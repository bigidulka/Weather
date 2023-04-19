from weatherDataWAPI import WeatherData
from location import Location
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui
import requests


class Translate:
    def __init__(self, data_dict: WeatherData) -> None:
        self.language = data_dict.language
        self.coordinates = data_dict.coordinates

        self.data_dict = data_dict

    def get_current_translation(self):
        current_weather = self.data_dict.parse_current_weather()
        result = Location.get_name_time(self.coordinates, self.language)
        city_name, country_name = result["city"], result["country"]
        local_time = result["local_time"]

        if self.language == 'en':
            translation = {
                'nameCityCountry': f"{city_name}, {country_name}",
                'time': f"It is now {local_time}. Yesterday at this time {0}",
                'temp': current_weather.get('temp_c', ''),
                'condition': current_weather.get('condition:text', ''),
                'feels_like': f"Feels like {current_weather.get('feelslike_c', '')}"
            }
        elif self.language == 'ru':
            translation = {
                'nameCityCountry': f"{city_name}, {country_name}",
                'time': f"Сейчас {local_time}. Вчера в это время {0}",
                'temp': current_weather.get('temp_c', ''),
                'condition': current_weather.get('condition:text', ''),
                'feels_like': f"Ощущается как {current_weather.get('feelslike_c', '')}"
            }
        else:
            raise ValueError(f"Unsupported language: {self.language}")
        return translation

    def parse_daily_forecast(self) -> dict:
        daily_forecast = self.data_dict.parse_daily_forecast()
        forecast_buttons = {}
        for forecast_data in daily_forecast:
            button = QPushButton()
            button.setFlat(True)
            button.setText(
                f"date: {forecast_data['date']}\navg: {forecast_data['avgtemp_c']}")

            layout = QVBoxLayout()
            button.setLayout(layout)

            forecast_buttons[forecast_data['date']] = button

        return forecast_buttons

    def parse_hourly_forecast(self, date_str: str) -> dict:
        hourly_forecast = self.data_dict.parse_hourly_forecast(date_str)
        forecast_frames = {}
        for forecast_data in hourly_forecast:
            frame = QFrame()
            # устанавливаем уникальное имя для фрейма
            frame.setObjectName("h_scr_fr")
            layout = QVBoxLayout()
            frame.setLayout(layout)

            # Устанавливаем стиль для frame с помощью CSS-свойств
            frame.setStyleSheet("""
                #h_scr_fr:hover {
                    background-color: rgba(200, 200, 200, 0.3);
                }
            """)

            icon_url = f"https:{forecast_data['condition:icon']}"
            icon_pixmap = QPixmap()
            icon_pixmap.loadFromData(requests.get(icon_url).content)

            time_label = QLabel(forecast_data['time'][-5:])
            time_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            layout.addWidget(time_label)

            icon_label = QLabel()
            icon_label.setPixmap(icon_pixmap.scaled(icon_pixmap.width(), 50, Qt.AspectRatioMode.KeepAspectRatio))
            icon_label.setAlignment(
                Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
            layout.addWidget(icon_label)

            condition_label = QLabel(
                f"{forecast_data['temp_c']} {forecast_data['condition:text']}")
            condition_label.setAlignment(
                Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
            layout.addWidget(condition_label)

            forecast_frames[forecast_data['time']] = frame

        return forecast_frames
