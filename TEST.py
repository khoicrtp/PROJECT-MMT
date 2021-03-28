import requests
import credentials
import re
cities = ["London,uk", "Porto,pt", "Paris,fr"]
weather_dict = {}


def city_forecast(city):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q": "London,uk", "lat": "0", "lon": "0", "callback": "test",
                   "id": "2172797", "lang": "null", "units": "\"metric\" or \"imperial\"", "mode": "xml, html"}

    headers = {
        'x-rapidapi-key': "c42e0924b5msh24cc9ad4d84110ap176dd9jsn81a33abf34fd",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    print(response)
    return response.json()


for city in cities:
    weather_dict[city] = city_forecast(city)
