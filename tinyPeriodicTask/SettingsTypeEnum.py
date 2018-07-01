#!/usr/bin/python3
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class SettingsType(Enum):
    unknow = -1
    number = 0
    Interval = 1
    StartAt = 2
