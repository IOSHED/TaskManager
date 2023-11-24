import json

import openmeteo_requests
import requests_cache
from urllib.request import urlopen

from retry_requests import retry

from task.lib.calendar.Weather import Weather
from task.lib.calendar.interface import IParser


class ParseWeather(IParser):
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    open_meteo = openmeteo_requests.Client(session=retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
        "wind_speed_unit": "ms"
    }

    def __init__(self, latitude: float, longitude: float) -> None:
        self.params["latitude"] = latitude
        self.params["longitude"] = longitude

    def parse(self) -> 'Weather':
        responses = self.open_meteo.weather_api(self.url, params=self.params)
        response = responses[0]

        current = response.Current()
        current_temperature_2m = current.Variables(0).Value()
        current_relative_humidity_2m = current.Variables(1).Value()
        current_wind_speed_10m = current.Variables(2).Value()

        return Weather(current_temperature_2m, current_wind_speed_10m, current_relative_humidity_2m)


class ParseLocation(IParser):
    def __init__(self) -> None:
        self.latitude = None
        self.longitude = None

    def parse(self) -> 'ParseLocation':
        cords = json.load(urlopen('http://ipinfo.io/json'))['loc'].split(",")
        self.latitude, self.longitude = list(map(float, cords))
        return self
