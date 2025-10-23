#ILOVESUBSCRIPTIONSERVICESWOHOO!!!!
import json
import requests

#I will be incredibly smart here and simply plop my api key down on this python file which will go on github.
# I'm sure that this is the most secure way of doing this and i'm not just being lazy :p
apikey = "62f0ba3d42df8b7b47ea79597e7b32c3"
# ps: I will deactivate it when im done, please dont hang me for this.

municipality = input("Enter municipality name: ")
httpQueryMunicipality = f"https://api.openweathermap.org/geo/1.0/direct?q={municipality}&appid={apikey}"
try:
    result = requests.get(httpQueryMunicipality)
    if result.status_code==200:
        json_result = result.json()
        lat = json_result[0]["lat"]
        lon = json_result[0]["lon"]
        httpQueryWeather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}&units=metric"
        try:
            result = requests.get(httpQueryWeather)
            if result.status_code == 200:
                json_result = result.json()
                weather_desc = json_result["weather"][0]["description"]
                temp_cel = json_result["main"]["temp"]
                print(f"Weather: {weather_desc}")
                print(f"Temperature: {temp_cel} Celsius")
        except requests.exceptions.RequestException as e:
            print(f"Could not fetch weather in '{municipality}'.")
except requests.exceptions.RequestException as e:
    print(f"Could not find '{municipality}'.")