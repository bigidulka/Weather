from weatherDataWAPI import WeatherData
from location import Location
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QByteArray
from PyQt6 import QtWidgets, QtGui
from datetime import datetime

class Translate:
    def __init__(self, data_dict: WeatherData) -> None:
        self.language = data_dict.language
        self.coordinates = data_dict.coordinates
        self.data_dict = data_dict

    def get_current_translation(self):
        current_weather = self.data_dict.parse_current_weather()
        result = Location.get_name_time(self.coordinates, self.language)
        city_name, country_name = result["city"], result["country"]
        time_only = result["local_time"].strftime("%H:%M")

        if self.language == 'en':
            translation = {
                'nameCityCountry': f"{city_name}, {country_name}" if city_name is not None else f"{country_name}",
                'time': f"It is now {time_only}. Yesterday at this time {0}",
                'temp': current_weather.get('temp_c', ''),
                'condition': current_weather.get('condition:text', ''),
                'feels_like': f"Feels like {current_weather.get('feelslike_c', '')}"
            }
        elif self.language == 'ru':
            translation = {
                'nameCityCountry': f"{city_name}, {country_name}" if city_name is not None else f"{country_name}",
                'time': f"Сейчас {time_only}. Вчера в это время {0}",
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

            icon = QPixmap(forecast_data['condition:icon'].replace('//cdn.weatherapi.com', 'path').replace('\\', '/'))

            time_label = QLabel(forecast_data['time'][-5:])
            time_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            layout.addWidget(time_label)

            icon_label = QLabel()
            icon_label.setPixmap(icon.scaled(icon.width(), 50, Qt.AspectRatioMode.KeepAspectRatio))
            icon_label.setAlignment(
                Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
            layout.addWidget(icon_label)

            condition_label = QLabel(
                f"{forecast_data['temp_c']}° {forecast_data['condition:text']}")
            condition_label.setAlignment(
                Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
            layout.addWidget(condition_label)

            forecast_frames[forecast_data['time']] = frame

        return forecast_frames
