TinyPeriodicTask
================
Set a simple periodic execution of a function.

Status
------
In development

Features
--------
* Set a periodic task with or without parameter(s).
* Start a runner to call a task to a specified interval.
* Stop the runner as well as restart it.
* Change parameter(s) during running. 
* No external dependencies.
* Tested on Python 3.5 and 3.6.

Installation
------------
please read https://help.github.com/articles/cloning-a-repository/

.. code-block:: batch

    $ git clone https://github.com/fredericklussier/TinyPeriodicTask.git

In the future, I expect to have a setup using pip.

Working on (developping)
-------------------------
* Change Interval when running. (next version)
* having an option for logging the execution.
* Interprete other units time as interval: minutes, hour, day, ...
* Set interval to a particular time of the day, or date.
* Prepare a setup in pip

Concepts
--------
* interval: time in second between executions.
* callback: callable function to run once the interval is reach.

The interval time is running in a deamon thread. This to ensure
the time has no interference to the main execution, and vice versa.

By design, when you start a tinyPeriodicTask instance, 
the runner will call the callback function immediatly before waiting 
for the next interval. 

When you create an instance of TinyPeriodicTask, you can add
any parameters you need to use when executing the callback. like this:

.. code-block:: python
    task = TinyPeriodicTask(3, task, message='that') 
    # this will call the task function every 3 seconds 
    #  using message as parameter.

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

If the runner is stopped, it will restart. If it is already started, it will do nothing.

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

Extra-fonctionnalities:
-----------------------
Changing interval will running
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can change the interval value during the runner execution.
This is usefull when you want to change the rhythm over time:
let say every 5 seconds during the day to 3600 (1hour) during 
the night. however, TinyPeriodicTask does not take those 
conditions (day and night) yet. So you have to manage them in your code.

.. code-block:: python

  tinyPeriodicTask.interval = 3600 #1 hour

Changing parameter(s) will running
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Let you change the parameter value.

This will restart the runner once the parameters changed. 

.. code-block:: python

  tinyPeriodicTask.useThis(*args, **kwargs)

+ ***args, **kwargs** parameter(s) to use when executing the callback function.
+ **Exception** If callback is not a callable function