#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import unittest
from datetime import datetime, timedelta

from tinyPeriodicTask.IntervalSettings import IntervalSettings
from tinyPeriodicTask.IntervalUnitEnum import IntervalUnit


class IntervalSettingsTest(unittest.TestCase):

    """
    Verify Properties
    """
    def testIntervalProperty_ShouldReturnDefaultInterval(self):
        # Arrange

        # Action
        settings = IntervalSettings(-1)

        # Assert
        self.assertEqual(settings.interval, 1)
        self.assertEqual(settings.unit, IntervalUnit.second)
        self.assertEqual(settings._mutiplicateur, 1)

    def testIntervalProperty_When0_ShouldReturnDefaultInterval(self):
        # Arrange

        # Action
        settings = IntervalSettings(0)

        # Assert
        self.assertEqual(settings.interval, 1)
        self.assertEqual(settings.unit, IntervalUnit.second)
        self.assertEqual(settings._mutiplicateur, 1)

    def testIntervalProperty_whenNoOption_ShouldReturnDefaultInterval(self):
        # Arrange

        # Action
        settings = IntervalSettings(5)

        # Assert
        self.assertEqual(settings.interval, 5)
        self.assertEqual(settings.unit, IntervalUnit.second)
        self.assertEqual(settings._mutiplicateur, 1)

    def testIntervalProperty_WhenMinutes_ShouldPrepareForMinutes(self):
        # Arrange

        # Action
        settings = IntervalSettings(12, IntervalUnit.minute)

        # Assert
        self.assertEqual(settings.interval, 12)
        self.assertEqual(settings.unit, IntervalUnit.minute)
        self.assertEqual(settings._mutiplicateur, 60)

    def testIntervalProperty_WhenHours_ShouldPrepareForHours(self):
        # Arrange

        # Action
        settings = IntervalSettings(12, IntervalUnit.hour)

        # Assert
        self.assertEqual(settings.interval, 12)
        self.assertEqual(settings.unit, IntervalUnit.hour)
        self.assertEqual(settings._mutiplicateur, 3600)

    def testIntervalProperty_WhenDays_ShouldPrepareForDays(self):
        # Arrange

        # Action
        settings = IntervalSettings(7, IntervalUnit.day)

        # Assert
        self.assertEqual(settings.interval, 7)
        self.assertEqual(settings.unit, IntervalUnit.day)
        self.assertEqual(settings._mutiplicateur, 86400)

    def testIntervalProperty_WhenOutsideUnit_ShouldPrepareForDefaultUnit(self):
        # Arrange
        with self.assertRaises(AssertionError):
            # Action
            settings = IntervalSettings(7, 5)

            # Assert from unittest when assert is trigged

    """
    Verify getValue
    """
    def testGetValue_ShouldReturnPropertiesValue(self):
        # Arrange
        expectedValue = {'interval': 7, 'unit': 'day'}
        setting = IntervalSettings(7, IntervalUnit.day)

        # Action
        actualValue = setting.getValue()

        # Assert
        self.assertEqual(actualValue, expectedValue)

    """
    Verify equality
    """
    def testEquality_ShouldReturnTrue(self):
        # Arrange
        settings = IntervalSettings(7, IntervalUnit.day)

        # Action
        actualValue = isinstance(settings, IntervalSettings)

        # Assert
        self.assertTrue(actualValue)

    """
    Verify nextRunAt
    """
    def testNextRunAt_WhenSeconds_ShouldReturnDateOfTheNextRun(self):
        # Arrange
        expectedValue = (
            datetime.now() + timedelta(seconds=7))
        settings = IntervalSettings(7)

        # Action
        actualValue = settings.nextRunAt()

        # Assert
        self.assertEqual(actualValue.replace(microsecond=0),
                         expectedValue.replace(microsecond=0))

    def testNextRunAt_WhenFractionSeconds_ShouldReturnDateOfTheNextRun(self):
            # Arrange
        expectedValue = (
            datetime.now() + timedelta(seconds=0.1))
        settings = IntervalSettings(0.1)

        # Action
        actualValue = settings.nextRunAt()

        # Assert
        self.assertEqual(actualValue.replace(microsecond=0),
                         expectedValue.replace(microsecond=0))
        self.assertIn(
            (actualValue.microsecond - expectedValue.microsecond),
            range(0, 9999)
        )

    def testNextRunAt_WhenMinutes_ShouldReturnDateOfTheNextRun(self):
        # Arrange
        expectedValue = (
            datetime.now() + timedelta(seconds=180))
        settings = IntervalSettings(3, IntervalUnit.minute)

        # Action
        actualValue = settings.nextRunAt()

        # Assert
        self.assertEqual(actualValue.replace(microsecond=0),
                         expectedValue.replace(microsecond=0))

    def testNextRunAt_WhenHours_ShouldReturnDateOfTheNextRun(self):
        # Arrange
        expectedValue = (
            datetime.now() + timedelta(seconds=7200))
        settings = IntervalSettings(2, IntervalUnit.hour)

        # Action
        actualValue = settings.nextRunAt()

        # Assert
        self.assertEqual(actualValue.replace(microsecond=0),
                         expectedValue.replace(microsecond=0))

    def testNextRunAt_WhenDays_ShouldReturnDateOfTheNextRun(self):
        # Arrange
        expectedValue = (
            datetime.now() + timedelta(seconds=86400))
        settings = IntervalSettings(1, IntervalUnit.day)

        # Action
        actualValue = settings.nextRunAt()

        # Assert
        self.assertEqual(actualValue.replace(microsecond=0),
                         expectedValue.replace(microsecond=0))
