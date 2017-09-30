#!/usr/bin/python3
# -*- coding: utf-8 -*-
import functools
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
  from PeriodicTask import PeriodicTask

  #The function to periodically run
  def task(message='this'):
    print("I'm working on {0}".format(message))

  task = TinyPeriodicTask(3, task)
  task.start()

  task2 = TinyPeriodicTask(3, task, message='that')
  task2.start()

  try:
    #Keep the main process alive
    # otherwise the task will be executed only one time
    while True:
      time.sleep(0.5)

  except KeyboardInterrupt:
     task.stop()
"""


class TinyPeriodicTask(object):
    def __init__(self, interval, callback, *args, **kwargs):
        """
        Set a periodic execution of a task.

        :param int interval: time in second between execution.
        :param func callback: callable function to call once the interval
         is reach.
        :param *args, **kwargs: parameter(s) to use when executing the
         callback function.
        """
        self._interval = interval if interval > 0 else 1
        self._callback = functools.partial(callback, *args, **kwargs)
        # End the thread once setted.
        self._ceaseContinuous = threading.Event()

    def __del__(self):
        self.stop()
        self._ceaseContinuous = None

    def start(self):
        """
        Start the periodic runner
        """
        if self._ceaseContinuous.is_set():
            self._ceaseContinuous.clear()  # restart

        class ScheduleThread(threading.Thread):
            @classmethod
            def run(cls):
                while not self._ceaseContinuous.is_set():
                    self._run()
                    time.sleep(self._interval)

        scheduleThread = ScheduleThread()
        scheduleThread.setDaemon(True)
        scheduleThread.start()

    def _run(self):
        self._callback()

    def stop(self):
        """
        Stop the periodic runner
        """
        self._ceaseContinuous.set()