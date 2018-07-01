#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import unittest
from datetime import datetime, timedelta

from tinyPeriodicTask.IntervalSettings import IntervalSettings
from tinyPeriodicTask.IntervalUnitEnum import IntervalUnit
from tinyPeriodicTask import TinyPeriodicTask


class testPeriodicInterval(unittest.TestCase):

    """
    Run periodic task using Interval settings
    """
    def testRunner_UsingIntervalSettings_ShouldRun(self):
        # Arrange
        count = 0

        def callableFunction():
            nonlocal count
            count += 1

        # Execute callback each 0.5 second
        settings = IntervalSettings(0.5, IntervalUnit.second)
        task = TinyPeriodicTask(settings, callableFunction)

        # Action
        task.start()

        while count < 5:
            time.sleep(0.1)

        task.stop()

        # Assert
        self.assertEqual(count, 5)
