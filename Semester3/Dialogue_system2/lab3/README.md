# Use API to get Temperature info with https://openweathermap.org/

## example in Python3

from urllib.request import urlopen as Request

import json

from tdm.tdmlib import DeviceWHQuery 

### ---------------------
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s' % (city,country)

response = Request(url)

### ---------------------


data = b'{coord':....} binrary data
### data = response.read()


 

 now data is string
### data = data.decode('utf-8')


### ---------------------
data_dict = json.loads(data)

return data_dict
