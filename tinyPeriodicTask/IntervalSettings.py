#!/usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
# from tinyPeriodicTask import IntervalUnitEnum
from .IntervalUnitEnum import IntervalUnit


class IntervalSettings(object):
    def __init__(self, interval, unit=IntervalUnit.getDefault()):
        self.interval = interval if (interval > 0) else 1
        self.unit = unit
        self._mutiplicateur = self.__getMultiplicateur(unit)

    def __getMultiplicateur(self, unit):
        assert isinstance(unit, IntervalUnit)
        values = [1, 60, 3600, 86400]
        return values[unit.value]

    def nextRunAt(self):
        seconds = self.interval * self._mutiplicateur
        return (datetime.now() +
                timedelta(seconds=seconds))

    def getValue(self):
        return {'interval': self.interval, 'unit': self.unit.name}
