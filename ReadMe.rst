TinyPeriodicTask
================
Set a simple periodic execution of a function.


Concepts
--------
* interval: time in second between executions.
* callback: callable function to call once the interval is reach.

The interval time is running in a deamon thread. This to ensure
the time has no interference to the main execution, and vice versa.

When you create an instance of TinyPeriodicTask, you can add
any parameters you need to use when executing the callback. like this:

.. code-block:: python

    task = TinyPeriodicTask(3, task, message='that') 

Usage
-----

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
        #Keep the main process alive 
        # otherwise the task will be executed only one time
        while True:
            time.sleep(0.5)

    except KeyboardInterrupt:
        task.stop()

Detail
------
init
~~~~~~~~
Set a periodic execution of a task.

.. code-block:: python

  class TinyPeriodicTask(interval, callback, *args, **kwargs)

+ **interval** (number) time in second between execution. 0 or negatif number is changed to 1.
+ **callback** (function) callable function to call once the interval is reach.
+ ***args, **kwargs** parameter(s) to use when executing the callback function.
+ **Exception** If callback is not a callable function

start
~~~~~~~~
Start the periodic runner

If the runner is stopped, it will restart.

.. code-block:: python

  tinyPeriodicTask = TinyPeriodicTask(5, anyCallback)
  tinyPeriodicTask.start()

stop
~~~~~~~~
Stop or pause the periodic runner.

.. code-block:: python

  tinyPeriodicTask = TinyPeriodicTask(5, anyCallback)
  tinyPeriodicTask.start()
  ...
  tinyPeriodicTask.stop()