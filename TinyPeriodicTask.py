#!/usr/bin/python3
# -*- coding: utf-8 -*-
import functools
from datetime import datetime, timedelta
import time
import threading

"""
Set a simple periodic execution of a function.

interval: time in second between executions.
callback: callable function to call once the interval is reach.

The interval time is running in a deamon thread. This to ensure
the time has no interference to the main execution, and vice versa.

When you create an instance of TinyPeriodicTask, you can add
any parameters you need to use when executing the callback. like this:
  .. code-block:: python
    task2 = TinyPeriodicTask(3, task, message='that') 

Usage:
.. code-block:: python

    from TinyPeriodicTask import TinyPeriodicTask

    #The function to periodically run
    def task(message='this'):
        print("I'm working on {0}".format(message))

    task = TinyPeriodicTask(3, task)
    task.start()

    task2 = TinyPeriodicTask(3, task, message='that')
    task2.start()

    try:
        print('Execution en cours')
        #Keep the main process alive
        # otherwise the task will be executed only one time
        while True:
            time.sleep(0.5)

    except KeyboardInterrupt:
        task1.stop()
        task2.stop()
        print('Loop stopped')

Result:

.. code-block:: batch

    $ python exemple.py
    I'm working on that
    Execution en cours
    I'm working on this
    I'm working on this
    I'm working on that
    I'm working on this
    I'm working on this
    I'm working on that
    I'm working on this
    I'm working on this
    I'm working on that
    I'm working on this
    Loop stopped
"""


class TinyPeriodicTask(object):
    def __init__(self, interval, callback, *args, **kwargs):
        """
        Set a periodic execution of a task.

        :param int interval: time in second between executions.
        :param func callback: callable function to call once the interval
         is reach.
        :param *args, **kwargs: parameter(s) to use when executing the
         callback function.
        """
        self._setInterval(interval)
        self._isRunning = False
        self._callback = functools.partial(callback, *args, **kwargs)
        # End the thread once setted.
        self._cease = threading.Event()

    @property
    def isRunning(self):
        """
        return true when runner is running otherwise false.
        """
        return self._isRunning

    @property
    def interval(self):
        """
        this is the interval property that mention to the runner
        the time in second between executions.
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        if self._isRunning:
            self.stop()
            self._setInterval(interval)
            self.start()
        else:
            self._setInterval(interval)

    def _setInterval(self, interval):
        self._interval = interval if interval > 0 else 1

    def __del__(self):
        self.stop()
        self._cease = None

    def start(self):
        """
        Start the periodic runner
        """
        if self._isRunning:
            return

        if self._cease.is_set():
            self._cease.clear()  # restart

        class Runner(threading.Thread):
            @classmethod
            def run(cls):
                nextRunAt = cls.setNextRun()

                while not self._cease.is_set():
                    if datetime.now() >= nextRunAt:
                        self._run()
                        nextRunAt = cls.setNextRun()

            @classmethod
            def setNextRun(cls):
                return datetime.now() + \
                    timedelta(seconds=self._interval)

        runner = Runner()
        runner.setDaemon(True)
        runner.start()
        self._isRunning = True

    def _run(self):
        self._callback()

    def useThis(self, *args, **kwargs):
        """
        Change parameter of the callback function.

        :param *args, **kwargs: parameter(s) to use when executing the
         callback function.
        """
        self._callback = functools.partial(self._callback, *args, **kwargs)

    def stop(self):
        """
        Stop the periodic runner
        """
        self._cease.set()
        time.sleep(0.1)  # let the thread closing correctly.
        self._isRunning = False
