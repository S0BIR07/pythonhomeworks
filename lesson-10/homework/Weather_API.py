'''import requests
import json
from Cities import capital_cities

city = input("Enter a capital city: ").lower()
try:
    lat = capital_cities[city.capitalize()]["lat"]
    lon = capital_cities[city.capitalize()]["lon"]
except KeyError:
    raise ValueError("Invalid capital city!")
appid = "c80dba7b6ff3fb963f226fb50da0f4ab"
url = "https://api.openweathermap.org/data/2.5/forecast/daily?"
params = {
    "appid": appid,
    "lat": lat,
    "lon" : lon,
    "units":"metric" #To get tempereture in celsius
}
response = requests.get(url, params=params)
if response.status_code==200:
    data = response.json()
    print("Daily weather info: ")
    print(f"Weather description: {data['list'][0]['weather'][0]['description']}")
    print(f"Temperature (day): {round(data['list'][0]['temp']['day'], 1)} °C")
    print(f"Temperature (night): {round(data['list'][0]['temp']['night'], 1)} °C")
    print(f"Humidity: {data['list'][0]['humidity']} %")
    print(f"Wind speed: {data['speed']} m/s")
else:
    print(f"Error: {response.status_code} - {response.text}")'''




import requests
import json
from Cities import capital_cities

city = input("Enter a capital city: ").lower()
try:
    lat = capital_cities[city.capitalize()]["lat"]
    lon = capital_cities[city.capitalize()]["lon"]
except KeyError:
    raise ValueError("Invalid capital city!")

appid = "c80dba7b6ff3fb963f226fb50da0f4ab"

# Correct URL for the forecast
url = "https://api.openweathermap.org/data/2.5/onecall"

params = {
    "appid": appid,
    "lat": lat,
    "lon": lon,
    "units": "metric"  # To get temperature in Celsius
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Daily weather info: ")
    # Assuming the daily forecast is in the "daily" field (as per the onecall API)
    print(f"Weather description: {data['daily'][0]['weather'][0]['description']}")
    print(f"Temperature (day): {round(data['daily'][0]['temp']['day'], 1)} °C")
    print(f"Temperature (night): {round(data['daily'][0]['temp']['night'], 1)} °C")
    print(f"Humidity: {data['daily'][0]['humidity']} %")
    print(f"Wind speed: {data['daily'][0]['wind_speed']} m/s")
else:
    print(f"Error: {response.status_code} - {response.text}")
