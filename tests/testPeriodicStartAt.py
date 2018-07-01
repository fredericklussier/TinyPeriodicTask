#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import unittest
from datetime import datetime, timedelta

from tinyPeriodicTask.StartAtSettings import StartAtSettings
from tinyPeriodicTask import TinyPeriodicTask


class testPeriodicStartAt(unittest.TestCase):

    """
    Set a periodic task using StartAt settings
    """
    def testPeriodicTask_UsingStartAtSettings_ShouldSetIt(self):
        # Arrange
        count = 0

        def callableFunction():
            pass

        # Execute callback each day specific time
        expectedValue = (
            datetime.now().replace(second=0, microsecond=0) +
            timedelta(hours=1, minutes=10))
        settings = StartAtSettings(expectedValue.strftime("%H:%M"))

        # Action
        task = TinyPeriodicTask(settings, callableFunction)

        # Assert
        self.assertEqual(
            task.interval['time'], expectedValue.strftime("%H:%M")
        )
