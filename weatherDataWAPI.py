import requests
from typing import Union
from location import Location


class WeatherData:
    API_KEY = '487da948423c4322b24221408231703 123'

    def __init__(self, language: str, text: str) -> None:
        self.text = text
        self.coordinates = None
        self.language = language
        self.data = self.__req_get_weather_data()

    def __req_get_weather_data(self) -> Union[dict, str]:
        if self.text is None:
            url = f'http://api.weatherapi.com/v1/forecast.json?key={WeatherData.API_KEY}&units=metric&days=14&lang={self.language}&q=auto:ip'
        else:
            self.coordinates = Location.get_coor_city(self.text)
            url = f'http://api.weatherapi.com/v1/forecast.json?key={WeatherData.API_KEY}&units=metric&days=14&lang={self.language}&q={self.coordinates[0]},{self.coordinates[1]}'

        try:
            with requests.get(url) as response:
                response.raise_for_status()
                json_data = response.json()
                if self.text is None:
                    self.coordinates = (
                        json_data['location']['lat'], json_data['location']['lon'])
                return json_data
        except requests.exceptions.HTTPError as error:
            return f'HTTP error occurred: {error}'

    def parse_current_weather(self) -> dict:
        return {
            'last_updated': self.data['current']['last_updated'],
            'last_updated_epoch': self.data['current']['last_updated_epoch'],
            'temp_c': self.data['current']['temp_c'],
            'feelslike_c': self.data['current']['feelslike_c'],
            'condition:text': self.data['current']['condition']['text'],
            'condition:icon': self.data['current']['condition']['icon'],
            'wind_kph': self.data['current']['wind_kph'],
            'wind_dir': self.data['current']['wind_dir'],
            'pressure_mb': self.data['current']['pressure_mb'],
            'precip_mm': self.data['current']['precip_mm'],
            'humidity': self.data['current']['humidity'],
            'cloud': self.data['current']['cloud'],
            'is_day': self.data['current']['is_day'],
            'gust_kph': self.data['current']['gust_kph'],
            'location': {
                'name': self.data['location']['name'],
                'region': self.data['location']['region'],
                'country': self.data['location']['country'],
                'localtime': self.data['location']['localtime']
            }
        }

    def parse_daily_forecast(self) -> list:
        forecasts = []
        for forecast in self.data['forecast']['forecastday']:
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
