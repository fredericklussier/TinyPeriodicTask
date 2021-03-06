TinyPeriodicTask
================


.. image:: https://travis-ci.org/fredericklussier/TinyPeriodicTask.svg?branch=master
    :target: https://travis-ci.org/fredericklussier/TinyPeriodicTask

.. image:: https://coveralls.io/repos/github/fredericklussier/TinyPeriodicTask/badge.svg?branch=master
    :target: https://coveralls.io/github/fredericklussier/TinyPeriodicTask?branch=master

.. image:: https://badge.fury.io/py/tinyPeriodicTask.svg
    :target: https://badge.fury.io/py/tinyPeriodicTask

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

.. code-block:: batch

    pip install tinyPeriodicTask

If you want all, please read https://help.github.com/articles/cloning-a-repository/

Concepts
--------
* interval: time in second between executions.
* callback: callable function to run once the interval is reach.

The interval time is running in a deamon thread. This to ensure
the time has no interference to the main execution, and vice versa.

By design, when you start a tinyPeriodicTask instance, 
the runner will delay the first call to the callback function 
according to the interval.

When you create an instance of TinyPeriodicTask, you can add
any parameters you need to use when executing the callback. like this:

.. code-block:: python
    task = TinyPeriodicTask(3, task, message='that') 
    # this will call the task function every 3 seconds 
    #  using message as parameter.

Usage
-----

.. code-block:: python

    from tinyPeriodicTask import TinyPeriodicTask

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

Settings:
~~~~~~~~~
Create and transmit a setting instance.

1- every unit
~~~~~~~~~
Set an interval specifying its unit (second, minute, hour, day)

.. code-block:: python

    from tinyPeriodicTask.IntervalSettings import IntervalSettings
    from tinyPeriodicTask.IntervalUnitEnum import IntervalUnit
    from tinyPeriodicTask import TinyPeriodicTask

    settings = IntervalSettings(5, IntervalUnit.hour)
    task = TinyPeriodicTask(settings, yourTaskFunction)

2- every day at
~~~~~~~~~
Set a job every day

.. code-block:: python

    from tinyPeriodicTask.StartAtSettings import StartAtSettings
    from tinyPeriodicTask import TinyPeriodicTask

    settings = StartAtSettings("15:30")
    task = TinyPeriodicTask(settings, yourTaskFunction)

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
Changing interval while running
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can change the interval value during the runner execution.
This is usefull when you want to change the rhythm over time:
let say every 5 seconds during the day to 3600 (1hour) during 
the night. however, TinyPeriodicTask does not take those 
conditions (day and night) yet. So you have to manage them in your code.

.. code-block:: python

  tinyPeriodicTask.interval = 3600 #1 hour

Changing parameter(s) while running
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Let you change the parameter value.

This will restart the runner once the parameters changed. 

.. code-block:: python

  tinyPeriodicTask.useThis(*args, **kwargs)

+ ***args, **kwargs** parameter(s) to use when executing the callback function.
+ **Exception** If callback is not a callable function

License
-------
Distributed under the MIT license: https://opensource.org/licenses/MIT

Copyright (c) 2017 Frédérick Lussier (www.linkedin.com/in/frederick-lussier-757b849)