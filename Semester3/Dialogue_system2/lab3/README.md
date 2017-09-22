### Use API to get Temperature info.

#example in Python3

from urllib.request import urlopen as Request

url = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s' % (city,country)
response = Request(url)
data = response.read()

return json.loads(data)
