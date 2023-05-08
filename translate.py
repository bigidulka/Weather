from weatherDataWAPI import WeatherData
from location import Location
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QSize
import datetime
import calendar

class Translate:
    def __init__(self, data_dict: WeatherData) -> None:
        self.language = data_dict.language
        self.coordinates = data_dict.coordinates
        self.data_dict = data_dict

    @staticmethod
    def translation_from_the_front(language):
        translations = {
            'en': {"search_placeholder": "Search",
                   "forecast_several_days": "Forecast for {n} days",
                   "hourly_forecast": "Hourly forecast for {n}",
                   "not_found": "Not found",
                   "search_empty": "Search Empty",
                   "no_net": "Check your Internet connection"},
            'ru': {"search_placeholder": "Поиск",
                   "forecast_several_days": "Прогноз на {n} дней",
                   "hourly_forecast": "Почасовой прогноз на {n}",
                   "not_found": "Не найдено",
                   "search_empty": "Строка пустая",
                   "no_net": "Проверьте подключение к интернету"}
        }
        return translations[language]

    def get_current_translation(self):
        wind_directions = {
            'N': 'С',
            'NNE': 'ССВ',
            'NE': 'СВ',
            'ENE': 'ВСВ',
            'E': 'В',
            'ESE': 'ВЮВ',
            'SE': 'ЮВ',
            'SSE': 'ЮЮВ',
            'S': 'Ю',
            'SSW': 'ЮЮЗ',
            'SW': 'ЮЗ',
            'WSW': 'ЗЮЗ',
            'W': 'З',
            'WNW': 'ЗСЗ',
            'NW': 'СЗ',
            'NNW': 'ССЗ',
        }
        
        current_weather = self.data_dict.parse_current_weather()
        result = Location.get_name_time(self.coordinates, self.language)
        city_name = result["city"]
        country_name = result["country"]
        self.time_only = result["local_time"].strftime("%H:%M")
        temp = ('+' if float(current_weather.get('temp_c', 0)) > 0 else '') + str(current_weather.get('temp_c', '')) + '°'
        feels_like = f"{'+' if float(current_weather.get('feelslike_c', 0)) > 0 else ''}{current_weather.get('feelslike_c', '')}°"
        condition = current_weather.get('condition:text', '')
        
        self.tray_text = f"{city_name}, {self.time_only}\n{condition}, {temp}"

        translations = {
            'en': {
                'nameCityCountry': f"{city_name}, {country_name}" if city_name else f"{country_name}",
                'time': f"It is now {self.time_only}",
                'temp': f"{temp}",
                'condition': f"{condition}",
                'feels_like': f"Feels like {feels_like}",
                
                'windText': f"{current_weather.get('wind_kph', '')} m/s, {current_weather.get('wind_dir', '')}",
                'humText': f"{current_weather.get('humidity', '')}%",
                'pressText': f"{current_weather.get('pressure_mb', '')}mmHg Art."
            },
            'ru': {
                'nameCityCountry': f"{city_name}, {country_name}" if city_name else f"{country_name}",
                'time': f"Сейчас {self.time_only}",
                'temp': f"{temp}",
                'condition': f"{condition}",
                'feels_like': f"Ощущается как {feels_like}",
                
                'windText': f"{current_weather.get('wind_kph', '')}м/c, {wind_directions.get(current_weather.get('wind_dir', ''), '')}",
                'humText': f"{current_weather.get('humidity', '')}%",
                'pressText': f"{current_weather.get('pressure_mb', '')}ммРт. ст."
            }
        }
        return translations[self.language]

    def parse_daily_forecast(self, color) -> dict:
        weekdays = {
            'Monday': {'en': 'Mon', 'ru': 'Пн'},
            'Tuesday': {'en': 'Tue', 'ru': 'Вт'},
            'Wednesday': {'en': 'Wed', 'ru': 'Ср'},
            'Thursday': {'en': 'Thu', 'ru': 'Чт'},
            'Friday': {'en': 'Fri', 'ru': 'Пт'},
            'Saturday': {'en': 'Sat', 'ru': 'Сб'},
            'Sunday': {'en': 'Sun', 'ru': 'Вс'}
        }
        months = {
            'en': dict(zip(range(1, 13), calendar.month_abbr[1:])),
            'ru': dict(zip(range(1, 13), ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']))
        }

        self.daily_forecast = self.data_dict.parse_daily_forecast()
        forecast_buttons = {}
        for idx, forecast_data in enumerate(self.daily_forecast):
            date_obj = datetime.datetime.strptime(forecast_data['date'], '%Y-%m-%d')
            weekday_str = weekdays[date_obj.strftime('%A')][self.language] if idx > 0 else "Сегодня" if self.language == 'ru' else 'Today'
            month_str = months[self.language][date_obj.month]
            day_str = date_obj.day
            maxtemp_str = f"{'Макс' if self.language == 'ru' else 'Max'} {forecast_data['maxtemp_c']}°"
            mintemp_str = f"{'Мин' if self.language == 'ru' else 'Min'} {forecast_data['mintemp_c']}°"
            button = QPushButton(styleSheet="font-family: 'Verdana';",objectName="daily_button", minimumSize=QSize(170, 125))
            button_layout = QHBoxLayout(button)
            icon_layout = QVBoxLayout()
            icon_label = QLabel(pixmap=QPixmap(forecast_data['condition:icon'].replace('//cdn.weatherapi.com', 'path').replace('\\', '/')))
            icon_layout.addWidget(icon_label)
            button_layout.addLayout(icon_layout)
            separator = QFrame(styleSheet="background-color: rgba(255, 255, 255, 0.3);", objectName="separator")
            separator.setFrameShape(QFrame.Shape.VLine)
            separator.setMaximumWidth(1)
            button_layout.addWidget(separator)
            info_layout = QVBoxLayout()
            date_label = QLabel(f"<b>{weekday_str}, {day_str} {month_str}</b>", objectName="date_label", wordWrap=True)
            info_layout.addWidget(date_label)
            info_layout.addWidget(QLabel(maxtemp_str))
            info_layout.addWidget(QLabel(mintemp_str))
            info_layout.addWidget(QLabel(forecast_data['condition:text'], wordWrap=True))
            button_layout.addLayout(info_layout)
            color_air = "path\icons\\air_FILL0_wght400_GRAD0_opsz48.svg" if color == "black" else "path\icons\\air_FILL0_wght400_GRAD0_opsz48_negate.png"
            color_hum = "path\icons\\humidity_percentage_FILL0_wght400_GRAD0_opsz48.svg" if color == "black" else "path\icons\\humidity_percentage_FILL0_wght400_GRAD0_opsz48_negate.png"
            for icon_path, text_label_data in [(color_air, f"{forecast_data['maxwind_kph']}{'м/c' if self.language == 'ru' else 'm/s'}"),
                                               (color_hum, f"{forecast_data['avghumidity']}%")]:
                hbox_layout = QHBoxLayout()
                hbox_layout.setSpacing(0)
                hbox_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
                hbox_layout.addWidget(QLabel(pixmap=QPixmap(icon_path).scaled(20, 20), alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter))
                hbox_layout.addWidget(QLabel(text_label_data, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter))
                icon_layout.addLayout(hbox_layout)
            forecast_buttons[forecast_data['date']] = button
        return forecast_buttons

    def parse_hourly_forecast(self, date_str: str) -> dict:
        hourly_forecast = self.data_dict.parse_hourly_forecast(date_str)
        forecast_frames = {}
        for forecast_data in hourly_forecast:
            hour = int(forecast_data['time'][-5:-3])
            if hour >= int(self.time_only[:2]) and self.daily_forecast[0]['date'] == date_str or self.daily_forecast[0]['date'] != date_str:
                frame = QFrame(objectName="h_scr_fr")
                frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
                layout = QVBoxLayout()
                frame.setLayout(layout)
                frame.setStyleSheet('#h_scr_fr:hover {background-color:rgba(255, 255, 255, 0.5);} QLabel { font-family: "Verdana"; }')
                icon = QPixmap(forecast_data['condition:icon'].replace('//cdn.weatherapi.com', 'path').replace('\\', '/'))
                icon_label = QLabel(alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignRight)
                icon_label.setPixmap(icon.scaled(icon.width(), 45, Qt.AspectRatioMode.KeepAspectRatio))
                text_layout = QVBoxLayout()
                time_label = QLabel(forecast_data['time'][-5:], alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)
                text_layout.addWidget(time_label)
                condition_label = QLabel(('+' if float(forecast_data['temp_c']) > 0 else '') + str(forecast_data['temp_c']) + '°', alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
                condition_label.setWordWrap(True)
                text_layout.addWidget(condition_label)
                condition_label.setStyleSheet('font-weight: bold;  font-family: "Verdana";')
                icon_and_text_layout = QHBoxLayout()
                icon_and_text_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
                icon_and_text_layout.addWidget(icon_label)
                icon_and_text_layout.addLayout(text_layout)
                layout.addLayout(icon_and_text_layout)
                forecast_frames[forecast_data['time']] = frame
        return forecast_frames
