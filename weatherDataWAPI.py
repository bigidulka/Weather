import requests
from typing import Union, Tuple
from functools import lru_cache
import time


class WeatherData:
    def __init__(self, coordinates: tuple, language: str) -> None:
        self.coordinates = coordinates
        self.language = language

    def __get_weather_data(self, fetcher_method, parser_method) -> Union[dict, Tuple[str, int]]:
        data = fetcher_method()
        if isinstance(data, dict):
            return parser_method(data)
        return data

    def get_current_weather(self) -> Union[dict, Tuple[str, int]]:
        return self.__get_weather_data(lambda: WeatherDataFetcher(self.coordinates, self.language).get_current_weather(), WeatherDataParser.parse_current_weather)

    def get_hourly_forecast(self) -> Union[dict, Tuple[str, int]]:
        return self.__get_weather_data(lambda: WeatherDataFetcher(self.coordinates, self.language).get_hourly_forecast(), WeatherDataParser.parse_hourly_forecast)

    def get_daily_forecast(self) -> Union[dict, Tuple[str, int]]:
        return self.__get_weather_data(lambda: WeatherDataFetcher(self.coordinates, self.language).get_daily_forecast(), WeatherDataParser.parse_daily_forecast)

    def get_all_data(self) -> Union[dict, str, Tuple[str, int]]:
        current_weather = self.get_current_weather()
        hourly_forecast = self.get_hourly_forecast()
        daily_forecast = self.get_daily_forecast()

        if isinstance(current_weather, str):
            return current_weather
        elif isinstance(hourly_forecast, str):
            return hourly_forecast
        elif isinstance(daily_forecast, str):
            return daily_forecast

        return {
            'current_weather': current_weather,
            'hourly_forecast': hourly_forecast,
            'daily_forecast': daily_forecast,
        }


class WeatherDataFetcher:
    def __init__(self, coordinates: tuple, language: str) -> None:
        self.coordinates = coordinates
        self.language = language
        self.__api_key = '487da948423c4322b24221408231703'

    def __get_params(self) -> dict:
        return {'lang': self.language, 'q': f'{self.coordinates[0]}, {self.coordinates[1]}'}

    @lru_cache(maxsize=128)
    def __get_weather_data(self, url: str) -> Union[dict, Tuple[str, int]]:
        try:
            response = requests.get(url, params=self.__get_params())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as error:
            return (f'HTTP error occurred: {error}', error.response.status_code)

    def get_current_weather(self) -> Union[dict, Tuple[str, int]]:
        url = f'http://api.weatherapi.com/v1/current.json?key={self.__api_key}&units=metric'
        return self.__get_weather_data(url)

    def get_hourly_forecast(self) -> Union[dict, Tuple[str, int]]:
        url = f'http://api.weatherapi.com/v1/forecast.json?key={self.__api_key}&units=metric&forecast_days=1'
        return self.__get_weather_data(url)

    def get_daily_forecast(self) -> Union[dict, Tuple[str, int]]:
        url = f'http://api.weatherapi.com/v1/forecast.json?key={self.__api_key}&units=metric&days=14'
        return self.__get_weather_data(url)


class WeatherDataParser:
    @staticmethod
    def parse_current_weather(data: dict) -> dict:
        return {
            'last_updated': data['current']['last_updated'],
            'last_updated_epoch': data['current']['last_updated_epoch'],
            'temp_c': data['current']['temp_c'],
            'feelslike_c': data['current']['feelslike_c'],
            'condition:text': data['current']['condition']['text'],
            'condition:icon': data['current']['condition']['icon'],
            'wind_kph': data['current']['wind_kph'],
            'wind_dir': data['current']['wind_dir'],
            'pressure_mb': data['current']['pressure_mb'],
            'precip_mm': data['current']['precip_mm'],
            'humidity': data['current']['humidity'],
            'cloud': data['current']['cloud'],
            'is_day': data['current']['is_day'],
            'gust_kph': data['current']['gust_kph'],
            'location': {
                'name': data['location']['name'],
                'region': data['location']['region'],
                'country': data['location']['country'],
                'localtime': data['location']['localtime']
            }
        }

    @staticmethod
    def parse_daily_forecast(data: dict) -> list:
        forecasts = []
        for forecast in data['forecast']['forecastday']:
            forecasts.append({
                'date': forecast['date'],
                'maxtemp_c': forecast['day']['maxtemp_c'],
                'mintemp_c': forecast['day']['mintemp_c'],
                'avgtemp_c': forecast['day']['avgtemp_c'],
                'maxwind_kph': forecast['day']['maxwind_kph'],
                'totalprecip_mm': forecast['day']['totalprecip_mm'],
                'avghumidity': forecast['day']['avghumidity'],
                'condition:text': forecast['day']['condition']['text'],
                'condition:icon': forecast['day']['condition']['icon']
            })
        return forecasts

    @staticmethod
    def parse_hourly_weather_for_date(data: dict, date_str: str) -> list:
        hourly_data = data['forecast']['forecastday'][0]['hour']
        result = []
        for hour_data in hourly_data:
            if hour_data['time'][:10] == date_str:
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


weather_data = WeatherData((48.8566, 2.3522), 'ru')
weather_data.get_all_data()
