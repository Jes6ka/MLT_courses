from tdm.lib.device import DddDevice, DeviceWHQuery, DeviceAction


class HelloWorldDevice(DddDevice):
    def __init__(self):
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
    
    class SetTime(DeviceAction):
        PARAMETERS = ["hour_to_set", "minute_to_set"]
        def perform(self, hour, minute):
            self.device._time_hour = hour
            self.device._time_minute = minute
            return True
            
    class SetAlarm(DeviceAction):
        PARAMETERS = ["hour_to_set", "minute_to_set"]
        def perform(self, hour, minute):
            self.device._alarm_hour = hour
            self.device._alarm_miniute = minute
			self._alarm_is_set = True
            return True




## this is original

from tdm.lib.device import DddDevice, DeviceWHQuery, DeviceAction


class HelloWorldDevice(DddDevice):
    def __init__(self):
        self.reset()
        
    def reset(self):
        self._time_hour = 00
        self._time_minute = 00
        #       self._alarm_hour = 00
        #       self._alarm_minute = 00
        #       self._alarm_is_set = False
        
    class current_time(DeviceWHQuery):
        def perform(self):
            time = '"%02d:%02d"' % (self.device._time_hour, self.device._time_minute)
            return [time]
    
    class SetTime(DeviceAction):
        PARAMETERS = ["hour_to_set", "minute_to_set"]
        def perform(self, hour, minute):
            self.device._time_hour = hour
            self.device._time_minute = minute
            return True
            
    # class SetAlarm(DeviceAction): COMPLETE THIS CLASS

	
