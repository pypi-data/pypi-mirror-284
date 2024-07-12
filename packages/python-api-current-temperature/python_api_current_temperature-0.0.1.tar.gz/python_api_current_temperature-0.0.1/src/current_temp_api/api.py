from .base import WeatherAPIBase
import requests


class OpenMeteo(WeatherAPIBase):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_current_temperature(self):
        params = {"latitude":self.latitude, "longitude":self.longitude, "current_weather":True}
        result = requests.get("https://api.open-meteo.com/v1/forecast", params=params)
        result_json = result.json()
        return result_json["current_weather"]["temperature"]


class OpenWeather(WeatherAPIBase):
    def __init__(self, latitude, longitude, **kwargs):
        self.latitude = latitude
        self.longitude = longitude
        self.api_token = kwargs.get("api_token")
    
    def get_current_temperature(self):
        params = {"lat": self.latitude, "lon": self.longitude, "appid": self.api_token}
        result = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
        result_json = result.json()
        return result_json["main"]["temp"]