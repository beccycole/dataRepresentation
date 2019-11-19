import requests
import json


url = "https://prodapi.metweb.ie/observations/newport-furnace/today"
response = requests.get(url)
data = response.json()
print(data)
for row in data:
    print (row["pressure"])

# filename = 'weatherReports.json'
# Writing JSON data
# f = open(filename, 'w')
# json.dump(data, f, indent=4)

