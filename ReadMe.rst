Set a simple periodic execution of a function.

interval: time in second between executions.
callback: callable function to call once the interval is reach.

The interval time is running in a deamon thread. This to ensure
the time has no interference to the main execution, and vice versa.

When you create an instance of TinyPeriodicTask, you can add
any parameters you need to use when executing the callback. like this:
    task = TinyPeriodicTask(3, task, message='that') 

Usage
-----

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