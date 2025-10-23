import json
import requests

httpQueryNorris = "https://api.chucknorris.io/jokes/random"
try:
    joke = requests.get(httpQueryNorris)
    if joke.status_code==200:
        json_joke = joke.json()
        print(json.dumps(json_joke["value"],indent=2))
except requests.exceptions.RequestException as e:
    print("Could not fetch norris fact.")