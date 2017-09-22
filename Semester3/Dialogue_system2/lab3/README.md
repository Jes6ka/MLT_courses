### Use API to get Temperature info.

#example in Python3

from urllib.request import urlopen as Request
import json

url = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s' % (city,country)
response = Request(url)

data = response.read()
#data = b'{coord':....} binrary data

data = data.decode('utf-8')
#now data is string

data_dict = json.loads(data)

return data_dict
