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
            time = '"%02d:%02d"' % (self.device._alarm_hour, self.device._alarm_minute)
            return [time]


    class current_time_oneshot(DeviceWHQuery):
        def perform(self):
            time = '"%02d:%02d"' % (self.device._time_hour, self.device._time_minute)
            return [time]

    class alarm_time_oneshot(DeviceWHQuery):
        def perform(self):
            time = '"%02d:%02d"' % (self.device._alarm_hour, self.device._alarm_minute)
            return [time]


    class SetTime(DeviceAction):
        PARAMETERS = ["hour_to_set", "minute_to_set"]
        def perform(self, hour, minute):# I cannot define name of function. already taken by system.e.g., look inside of grammar_eng.xml, action name 'top' is already used in action. without any 'perform' definition
            self.device._time_hour = hour
            self.device._time_minute = minute
            return True

    class SetAlarm(DeviceAction):
        PARAMETERS = ["hour_to_set", "minute_to_set"]
        def perform(self, hour, minute):    # it becomees   goal type="oneshot" in domain.xml
            self.device._alarm_hour = hour
            self.device._alarm_minute = minute
            self.device._alarm_is_set = True
            return True

    class SetTimeOneshot(DeviceAction):
        PARAMETERS = ["hour_to_set", "minute_to_set"]
        def perform(self, hour, minute):# I cannot define name of function. already taken by system.e.g., look inside of grammar_eng.xml, action name 'top' is already used in action. without any 'perform' definition
            self.device._time_hour = hour
            self.device._time_minute = minute
            return True

    class SetAlarmOneshot(DeviceAction):
        PARAMETERS = ["hour_to_set", "minute_to_set"]
        def perform(self, hour, minute):    # it becomees   goal type="oneshot" in domain.xml
            self.device._alarm_hour = hour
            self.device._alarm_minute = minute
            self.device._alarm_is_set = True
            return True
