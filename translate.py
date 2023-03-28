from weatherDataWAPI import WeatherData
from typing import Union
from location import Location
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton


class Translate:
    def __init__(self, data_dict: WeatherData) -> None:
        self.language = data_dict.language
        self.coordinates = data_dict.coordinates

        self.current_weather = data_dict.get_current_weather()
        self.daily_forecast = data_dict.get_daily_forecast()

    def get_current_translation(self):
        result = Location.get_name_time(self.coordinates, self.language)
        city_name, country_name = result["city"], result["country"]
        local_time = result["local_time"]

        if self.language == 'en':
            translation = {
                'nameCityCountry': f"{city_name}, {country_name}",
                'time': f"It is now {local_time}. Yesterday at this time {0}",
                'temp': self.current_weather.get('temp_c', ''),
                'condition': self.current_weather.get('condition:text', ''),
                'feels_like': f"Feels like {self.current_weather.get('feelslike_c', '')}"
            }
        elif self.language == 'ru':
            translation = {
                'nameCityCountry': f"{city_name}, {country_name}",
                'time': f"Сейчас {local_time}. Вчера в это время {0}",
                'temp': self.current_weather.get('temp_c', ''),
                'condition': self.current_weather.get('condition:text', ''),
                'feels_like': f"Ощущается как {self.current_weather.get('feelslike_c', '')}"
            }
        else:
            raise ValueError(f"Unsupported language: {self.language}")
        return translation

    def parse_daily_forecast(self) -> dict:
        forecast_buttons = {}
        for forecast_data in self.daily_forecast:
            button = QPushButton()
            button.setFlat(True)
            button.setText(
                f"date: {forecast_data['date']}\navg: {forecast_data['avgtemp_c']}")

            layout = QVBoxLayout()
            button.setLayout(layout)

            forecast_buttons[forecast_data['date']] = button

        return forecast_buttons

    def parse_hourly_forecast(self) -> list:
        pass
