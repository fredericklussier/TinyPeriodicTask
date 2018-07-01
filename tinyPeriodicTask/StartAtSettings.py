#!/usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta


class StartAtSettings(object):
    def __init__(self, timeStr):
        assert timeStr.find(":") > 0
        hour, minute = timeStr.split(':')
        self.hour = int(hour)
        assert 0 <= self.hour <= 23

        self.minute = int(minute)
        assert 0 <= self.minute <= 59

    def getValue(self):
        return {'time': '{:02d}:{:02d}'.format(self.hour, self.minute)}

    def nextRunAt(self):
        when = datetime.now().replace(
            hour=self.hour, minute=self.minute, second=0, microsecond=0)
        if (when < datetime.now()):
            when = when + timedelta(days=1)
        return when
