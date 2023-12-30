import requests
import json
import os
city_name = input("Enter the name of the city\n_:")
callable_url = f"http://api.weatherapi.com/v1/current.json?key=c33689ff82604764a17193057233012&q={city_name}&aqi=no"
data = requests.request("GET", callable_url).json()
print(type(data))

print(json.dumps(data, indent=4))
print(data["current"]["temp_c"])
os.system(f"spd-say 'Current temperature in {city_name} is {data['current']['temp_c']}' degrees Celsius")