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

example
{"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":741,"main":"Fog","description":"fog","icon":"50d"}],"base":"stations","main":{"temp":279.9,"pressure":1021,"humidity":93,"temp_min":276.15,"temp_max":283.15},"visibility":10000,"wind":{"speed":3.6,"deg":230,"gust":9.8},"clouds":{"all":0},"dt":1506059400,"sys":{"type":1,"id":5091,"message":0.0049,"country":"GB","sunrise":1506059230,"sunset":1506103082},"id":2643743,"name":"London","cod":200}
