from yaweather import YaWeather, cities
from typing import Tuple

class WeatherData(YaWeather):
    def __init__(self, country, city):
        ywm = YaWeather(api_key='69837bd5-2216-4f9d-b4bf-1d4ff578de56')
        
        coordinates = self.get_coordinates_city(country, city)
                
        self.forecast = ywm.forecast(coordinates)
    
    @classmethod
    def get_coordinates_city(self, country, city) -> Tuple[float, float]:
        country_class = getattr(cities, country, None)
        return country_class.cities()[city]
    
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
    def observation_time(self):
        return self.forecast.fact.observation_time

    @property
    def precipitation_type(self):
        return self.forecast.fact.prec_type

    @property
    def precipitation_strength(self):
        return self.forecast.fact.prec_strength