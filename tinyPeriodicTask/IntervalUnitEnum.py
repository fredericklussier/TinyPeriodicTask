#!/usr/bin/python3
# -*- coding: utf-8 -*-
from enum import Enum, unique


class IntervalUnit(Enum):
    second = 0
    minute = 1
    hour = 2
    day = 3

    @classmethod
    def getDefault(cls):
        return cls.second
