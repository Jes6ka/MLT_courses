from tdm.lib.device import DddDevice, DeviceWHQuery, DeviceAction


class HelloWorldDevice(DddDevice):
    def __init__(self):
        #seems like function DddDevice is making  "device" in this self object.
        self.reset()

    def reset(self):
        self._time_hour = 00
        self._time_minute = 00
        self._alarm_hour = 00
        self._alarm_minute = 00
        self._alarm_is_set = False

class current_time(DeviceWHQuery):
    def perform(self):
        time = '"%02d:%02d"' % (self.device._time_hour, self.device._time_minute)
        return [time]

class alarm_time(DeviceWHQuery):
    def perform(self):
        time = '"%02d:%02d"' % (self.device._time_hour, self.device._time_minute)
        return [time]

class SetTime(DeviceAction):
    PARAMETERS = ["hour_to_set", "minute_to_set"]
    def perform(self, hour, minute):
        self.device._time_hour = hour
        self.device._time_minute = minute
        return True
    def oneshot(self, hour, minute):
        self.device._time_hour = hour
        self.device._time_minute = minute
        return True

class SetAlarm(DeviceAction):
    PARAMETERS = ["hour_to_set", "minute_to_set"]
    def perform(self, hour, minute):
        self.device._time_hour = hour
        self.device._time_minute = minute
        return True
    def oneshot(self, hour, minute):    # it becomees   goal type="oneshot" in domain.xml
        self.device._time_hour = hour
        self.device._time_minute = minute
        return True
