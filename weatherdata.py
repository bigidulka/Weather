from yaweather import YaWeather, cities
from typing import Tuple
import pytz
import datetime
from timezonefinder import TimezoneFinder
import requests

class WeatherData(YaWeather):
    def __init__(self, coordinates):
        ywm = YaWeather(api_key='69837bd5-2216-4f9d-b4bf-1d4ff578de56')
        
        self.coordinates = coordinates
        
        try:
            self.forecast = ywm.forecast(self.coordinates)
        except requests.exceptions.ReadTimeout:
            pass

    @classmethod
    def get_coordinates_city(self, country, city) -> tuple[float, float]:
        country_class = getattr(cities, country, None)
        city_coord = country_class.cities().get(city)
        if not city_coord:
            return None
        return city_coord

    @property
    def observation_time(self):
        tf = TimezoneFinder(in_memory=True)
        timezone = tf.timezone_at(lat=self.coordinates[0], lng=self.coordinates[1])
        now = datetime.datetime.now(pytz.timezone(timezone))
        return now.strftime("%H:%M")

    @property
    def temperature(self):
        return self.forecast.fact.temp

    @property
    def feel_temperature(self):
        return self.forecast.fact.feels_like

    @property
    def cloudness(self):
        return self.forecast.fact.cloudness

    @property
    def pressure(self):
        return self.forecast.fact.pressure_mm

    @property
    def wind_speed(self):
        return self.forecast.fact.wind_speed

    @property
    def wind_gust(self):
        return self.forecast.fact.wind_gust

    @property
    def wind_direction(self):
        return self.forecast.fact.wind_dir

    @property
    def humidity(self):
        return self.forecast.fact.humidity

    @property
    def condition(self):
        return self.forecast.fact.condition

    @property
    def icon(self):
        return self.forecast.fact.icon

    @property
    def precipitation_type(self):
        return self.forecast.fact.prec_type

    @property
    def precipitation_strength(self):
        return self.forecast.fact.prec_strength