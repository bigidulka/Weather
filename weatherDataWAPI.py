import requests
from typing import Union
from location import Location


class WeatherData:
    API_KEY = '487da948423c4322b24221408231703'

    def __init__(self, language: str, coordinates: tuple) -> None:
        self.coordinates = coordinates
        self.language = language
        self.data = self.__req_get_weather_data()

    def __req_get_weather_data(self) -> Union[dict, str]:
        url = f'http://api.weatherapi.com/v1/forecast.json?key={WeatherData.API_KEY}&units=metric&days=14&lang={self.language}&q={self.coordinates[0]},{self.coordinates[1]}'
        try:
            with requests.get(url) as response:
                response.raise_for_status()
                json_data = response.json()
                return json_data
        except requests.exceptions.HTTPError as error:
            return f'{error}'
    
    def parse_current_weather(self) -> dict:
        current_data = self.data['current']
        location_data = self.data['location']
        return {
            'last_updated': current_data['last_updated'],
            'last_updated_epoch': current_data['last_updated_epoch'],
            'temp_c': current_data['temp_c'],
            'feelslike_c': current_data['feelslike_c'],
            'condition:text': current_data['condition']['text'],
            'condition:icon': current_data['condition']['icon'],
            'wind_kph': current_data['wind_kph'],
            'wind_dir': current_data['wind_dir'],
            'pressure_mb': current_data['pressure_mb'],
            'precip_mm': current_data['precip_mm'],
            'humidity': current_data['humidity'],
            'cloud': current_data['cloud'],
            'is_day': current_data['is_day'],
            'location': {
                'name': location_data['name'],
                'region': location_data['region'],
                'country': location_data['country'],
                'localtime': location_data['localtime']
            }
        }

    def parse_daily_forecast(self) -> list:
        forecasts = []
        for forecast in self.data['forecast']['forecastday']:
            day_data = forecast['day']
            forecasts.append({
                'date': forecast['date'],
                'maxtemp_c': day_data['maxtemp_c'],
                'mintemp_c': day_data['mintemp_c'],
                'avgtemp_c': day_data['avgtemp_c'],
                'maxwind_kph': day_data['maxwind_kph'],
                'totalprecip_mm': day_data['totalprecip_mm'],
                'avghumidity': day_data['avghumidity'],
                'condition:text': day_data['condition']['text'],
                'condition:icon': day_data['condition']['icon']
            })
        return forecasts

    def parse_hourly_forecast(self, date_str: str) -> list:
        hourly_data = self.data['forecast']['forecastday']
        result = []
        for day_data in hourly_data:
            if day_data['date'] == date_str:
                for hour_data in day_data['hour']:
                    result.append({
                        'time': hour_data['time'],
                        'temp_c': hour_data['temp_c'],
                        'condition:text': hour_data['condition']['text'],
                        'condition:icon': hour_data['condition']['icon'],
                        'wind_kph': hour_data['wind_kph'],
                        'wind_dir': hour_data['wind_dir'],
                        'pressure_mb': hour_data['pressure_mb'],
                        'precip_mm': hour_data['precip_mm'],
                        'humidity': hour_data['humidity'],
                        'cloud': hour_data['cloud'],
                        'is_day': hour_data['is_day'],
                    })
        return result