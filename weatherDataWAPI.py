import requests
from typing import Union, Tuple
from collections import namedtuple

WeatherDataResult = namedtuple('WeatherDataResult', ['data', 'status_code'])


class WeatherData:
    API_KEY = '487da948423c4322b24221408231703'

    def __init__(self, coordinates: tuple, language: str) -> None:
        self.coordinates = coordinates
        self.language = language

    def __req_get_weather_data(self) -> WeatherDataResult:
        url = f'http://api.weatherapi.com/v1/forecast.json?key={WeatherData.API_KEY}&units=metric&days=14&lang={self.language}&q={self.coordinates[0]},{self.coordinates[1]}'
        try:
            with requests.Session() as session:
                response = session.get(url)
                response.raise_for_status()
                return WeatherDataResult(data=response.json(), status_code=response.status_code)
        except requests.exceptions.HTTPError as error:
            return WeatherDataResult(data=f'HTTP error occurred: {error}', status_code=error.response.status_code)

    def __get_weather_data(self, parser_method) -> Union[dict, Tuple[str, int]]:
        data = self.__req_get_weather_data()
        if isinstance(data.data, dict):
            return parser_method(data.data)
        return data

    def get_current_weather(self) -> Union[dict, Tuple[str, int]]:
        return self.__get_weather_data(WeatherDataParser.parse_current_weather)

    def get_daily_forecast(self) -> Union[dict, Tuple[str, int]]:
        return self.__get_weather_data(WeatherDataParser.parse_daily_forecast)

    def get_hourly_forecast(self, date: str) -> Union[dict, Tuple[str, int]]:
        return self.__get_weather_data(WeatherDataParser.parse_hourly_forecast, date)


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
    def parse_hourly_forecast(data: dict, date_str: str) -> list:
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

data = WeatherData((55.755825, 37.617298), 'ru')
print(data.get_hourly_forecast('2023-04-01'))