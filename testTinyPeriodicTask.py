#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import unittest

from TinyPeriodicTask import TinyPeriodicTask


class TinyPeriodicTaskTest(unittest.TestCase):
    """
    Interval Property
    """
    def testIntervalProperty_ShouldReturnInterval(self):
        # Arrange
        def callableFunction():
            pass

        # Action
        task = TinyPeriodicTask(5, callableFunction)

        # Assert
        self.assertEqual(task.interval, 5)

    def testIntervalProperty_Using0_ShouldSetIntervalTo1(self):
        # Arrange
        def callableFunction():
            pass

        # Action
        task = TinyPeriodicTask(0, callableFunction)

        # Assert
        self.assertEqual(task.interval, 1)

    def testIntervalProperty_UsingNegativeInterval_ShouldSetIntervalTo1(self):
        # Arrange
        def callableFunction():
            pass

        # Action
        task = TinyPeriodicTask(-1, callableFunction)

        # Assert
        self.assertEqual(task.interval, 1)

    def testIntervalProperty_Set_ShouldSetInterval(self):
        # Arrange
        def callableFunction():
            pass

        task = TinyPeriodicTask(-1, callableFunction)

        # Action
        task.interval = 0.5

        # Assert
        self.assertEqual(task.interval, 0.5)

    """
    isRunning
    """
    def testIsRunningProperty_Init_ShouldReturnFalse(self):
        # Arrange
        def callableFunction():
            pass

        task = TinyPeriodicTask(-1, callableFunction)

        # Action
        expectedValue = task.isRunning

        # Assert
        self.assertFalse(expectedValue)

    def testIsRunningProperty_WhenRunning_ShouldReturnTrue(self):
        # Arrange
        def callableFunction():
            pass

        task = TinyPeriodicTask(-1, callableFunction)

        # Action
        task.start()
        expectedValue = task.isRunning
        task.stop()

        # Assert
        self.assertTrue(expectedValue)

    def testIsRunningProperty_WhenCeaseRunning_ShouldReturnFalse(self):
        # Arrange
        def callableFunction():
            pass

        task = TinyPeriodicTask(0.1, callableFunction)

        # Action
        task.start()
        task.stop()
        expectedValue = task.isRunning

        # Assert
        self.assertFalse(expectedValue)

    """
    Runner
    """
    def testRunner_ShouldAlmostBeTheIntervalTime(self):
        # Arrange
        start_time = 0
        count = 0

        def callableFunction():
            nonlocal count, start_time
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

    def testRunner_UsingNoParameter_ShouldExecuteTheCallbackFunction(self):
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

    def testRunner_UsingParameter_ShouldExecuteTheCallbackFunction(self):
        # Arrange
        count = 0

        def callableFunction(parameter):
            nonlocal count
            count += 1
            self.assertEqual(parameter, 12)

        # Execute the callback each 1 second
        task = TinyPeriodicTask(1, callableFunction, parameter=12)

        # Action
        task.start()

        while count < 5:
            time.sleep(0.5)

        task.stop()

        # Assert
        self.assertEqual(count, 5)

    def testRunner_RestartWhenRunning_ShouldDoNothing(self):
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

    def testRunner_ChangeInterval_ShouldUseTheNewInterval(self):
        # Arrange
        count = 0
        start_time = 0

        def callableFunction(parameter="this"):
            nonlocal count, start_time
            expected = 1 if count < 3 else 2
            if (count > 0 and count != 3):
                self.assertAlmostEqual(
                    time.time() - start_time, expected, 0, "when count {0}".format(count))
            count += 1
            start_time = time.time()

        # Execute the callback each 0.1 second
        task = TinyPeriodicTask(1, callableFunction)

        # Action
        start_time = time.time()
        task.start()

        while count < 5:
            if count == 3 and task.interval == 1:
                task.interval = 2
            time.sleep(0.01)

        task.stop()

    def testRunner_ChangeParameter_ShouldUseNewSetOfParameters(self):
        # Arrange
        count = 0

        def callableFunction(parameter):
            nonlocal count
            expected = 12 if count < 3 else 10
            self.assertEqual(parameter, expected)
            count += 1

        # Execute the callback each 0.1 second
        task = TinyPeriodicTask(0.1, callableFunction, parameter=12)

        # Action
        task.start()

        while count < 5:
            if count >= 3:
                task.useThis(parameter=10)
            time.sleep(0.01)

        task.stop()

        # Assert
        self.assertEqual(count, 5)

    def testRunner_Restart_ShouldStartTheExecution(self):
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
