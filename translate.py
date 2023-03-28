from weatherDataWAPI import WeatherData
from typing import Union
from location import Location
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout, QWidget


class Translate:
    def __init__(self, data_dict: WeatherData) -> None:
        self.data_dict = data_dict.get_all_data()
        self.language = data_dict.language
        self.coordinates = data_dict.coordinates

    def get_current_translation(self):
        result = Location.get_name_time(self.coordinates, self.language)
        city_name, country_name = result["city"], result["country"]
        current_weather = self.data_dict.get('current_weather', {})
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

    @staticmethod
    def parse_daily_forecast(data: dict) -> list:
        print(data)
        forecast_frames = []
        for forecast_data in data['forecast']['forecastday']:
            # Create the QFrame
            frame = QFrame()
            layout = QVBoxLayout()
            frame.setLayout(layout)

            # Add labels to the QFrame for the forecast data
            label = QLabel(f"Date: {forecast_data['date']}\nMax Temp: {forecast_data['day']['maxtemp_c']}°C\nMin Temp: {forecast_data['day']['mintemp_c']}°C\nAvg Temp: {forecast_data['day']['avgtemp_c']}°C\nMax Wind: {forecast_data['day']['maxwind_kph']} km/h\nTotal Precipitation: {forecast_data['day']['totalprecip_mm']} mm\nAvg Humidity: {forecast_data['day']['avghumidity']}\nCondition: {forecast_data['day']['condition']['text']}")
            layout.addWidget(label)

            # Create a QWidget to contain the QFrame
            widget = QWidget()
            widget.setLayout(layout)

            # Append the QFrame to the array
            forecast_frames.append(frame)

        return forecast_frames
