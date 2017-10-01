#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import unittest

from TinyPeriodicTask import TinyPeriodicTask


class TinyPeriodicTaskTest(unittest.TestCase):

    def testTime_ShouldAlmostBeTheIntervalTime(self):
        # Arrange
        start_time = 0
        count = 0

        def callableFunction():
            nonlocal count
            nonlocal start_time
            count += 1
            if count > 1:
                self.assertAlmostEqual(time.time() - start_time, 1, 0)
            start_time = time.time()

        # Execute the callback each 1 second
        task = TinyPeriodicTask(1, callableFunction)

        # Action
        start_time = time.time()
        task.start()

        while count < 5:
            time.sleep(0.5)

        task.stop()

        # Assert
        self.assertEqual(count, 5)

    def testStart_UsingNoParameter_ShouldExecuteTheCallbackFunction(self):
        # Arrange
        count = 0

        def callableFunction():
            nonlocal count
            count += 1

        # Execute callback each 0.5 second
        task = TinyPeriodicTask(0.5, callableFunction)

        # Action
        task.start()

        while count < 5:
            time.sleep(0.1)

        task.stop()

        # Assert
        self.assertEqual(count, 5)

    def testStart_TryToRestart_ShouldDoNothing(self):
            # Arrange
        count = 0

        def callableFunction():
            nonlocal count
            count += 1

        # Execute callback each 0.5 second
        task = TinyPeriodicTask(0.5, callableFunction)
        task.start()
        
        # Action
        task.start()

        while count < 5:
            time.sleep(0.1)

        task.stop()

        # Assert
        self.assertEqual(count, 5)

    def testStart_UsingParameter_ShouldExecuteTheCallbackFunction(self):
        # Arrange
        count = 0

        def callableFunction(parameter):
            nonlocal count
            count += 1
            self.assertEqual(parameter, 12)

        # Execute tnhe callback each 1 second
        task = TinyPeriodicTask(1, callableFunction, parameter=12)

        # Action
        task.start()

        while count < 5:
            time.sleep(0.5)

        task.stop()

        # Assert
        self.assertEqual(count, 5)

    def testReStart_ShouldStartTheExecution(self):
        # Arrange
        countCalled = 0

        def callableFunction():
            nonlocal countCalled
            countCalled += 1

        # Execute the callback each 1 second
        task = TinyPeriodicTask(1, callableFunction)

        # Action
        task.start()

        count = 0
        while count < 10:
            count += 1

            if count == 3:
                task.stop()

            if count == 6:
                task.start()

            time.sleep(0.5)

        task.stop()

        # Assert
        self.assertLess(countCalled, 7)
