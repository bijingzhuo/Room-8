import http.client
import json


conn = http.client.HTTPConnection("localhost", 9091)


conn.request("GET", "/")


response = conn.getresponse()

data = response.read()
cities = json.loads(data)

for city in cities:
    print(city)

conn.close()
