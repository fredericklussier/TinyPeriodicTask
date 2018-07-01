#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import unittest
from datetime import datetime, timedelta

from tinyPeriodicTask.StartAtSettings import StartAtSettings


class StartAtSettingsTest(unittest.TestCase):

    """
    Verify Properties
    """
    def testIntervalProperty_ShouldReturnDefaultInterval(self):
        # Arrange

        # Action
        settings = StartAtSettings('01:20')

        # Assert
        self.assertEqual(settings.hour, 1)
        self.assertEqual(settings.minute, 20)

    def testIntervalProperty_WhenBadSeparator_ShouldRaiseError(self):
        # Arrange
        with self.assertRaises(AssertionError):

            # Action
            settings = StartAtSettings('1,20')

            # Assert from unittest when assert is trigged

    def testIntervalProperty_WhenBadString_ShouldRaiseError(self):
        # Arrange
        with self.assertRaises(ValueError):

            # Action
            settings = StartAtSettings('now:true')

            # Assert from unittest when assert is trigged

    def testIntervalProperty_WhenBadMinutesString_ShouldRaiseError(self):
        # Arrange
        with self.assertRaises(ValueError):

            # Action
            settings = StartAtSettings('01:true')

            # Assert from unittest when assert is trigged

    def testIntervalProperty_WhenOutboundHour_ShouldRaiseError(self):
        # Arrange
        with self.assertRaises(AssertionError):

            # Action
            settings = StartAtSettings('24:00')

            # Assert from unittest when assert is trigged

    def testIntervalProperty_WhenOutboundMinutes_ShouldRaiseError(self):
        # Arrange
        with self.assertRaises(AssertionError):

            # Action
            settings = StartAtSettings('2:80')

            # Assert from unittest when assert is trigged

    """
    Verify getValue
    """
    def testGetValue_ShouldReturnValues(self):
        # Arrange
        expectedValue = {'time': '01:45'}

        # Action
        actualValue = StartAtSettings('1:45')

        # Assert
        self.assertEqual(actualValue.getValue(), expectedValue)

    """
    Verify equality
    """
    def testEquality_ShouldReturnTrue(self):
        # Arrange
        settings = StartAtSettings('14:45')

        # Action
        actualValue = isinstance(settings, StartAtSettings)

        # Assert
        self.assertTrue(actualValue)

    """
    Verify nextRunAt
    """
    def testNextRunAt_WhenTimePast_ShouldReturnDateOfTheNextRun(self):
        # Arrange
        expectedValue = (
            datetime.now().replace(second=0, microsecond=0) +
            timedelta(hours=-1, minutes=-10))

        settings = StartAtSettings(expectedValue.strftime("%H:%M"))

        # Action
        actualValue = settings.nextRunAt()

        # Assert
        # expect to start tomorrow since time is past today
        self.assertEqual(actualValue, expectedValue + timedelta(days=1))

    def testNextRunAt_WhenNextDay_ShouldReturnDateOfTheNextRun(self):
        # Arrange
        expectedValue = (
            datetime.now().replace(second=0, microsecond=0) +
            timedelta(hours=1, minutes=10))

        settings = StartAtSettings(expectedValue.strftime("%H:%M"))

        # Action
        actualValue = settings.nextRunAt()

        # Assert
        self.assertEqual(actualValue, expectedValue)
