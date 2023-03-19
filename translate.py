from weatherDataWAPI import WeatherData
from typing import Union
from location import Location


class Translate:
    def __init__(self, weather_data: WeatherData) -> None:
        self.data_dict = weather_data.get_all_data()
        self.language = weather_data.language
        self.coordinates = weather_data.coordinates

    def get_translation(self) -> Union[dict, str]:
        if isinstance(self.data_dict, tuple):
            return self.data_dict

        result = Location.get_name_time(self.coordinates, self.language)
        city_name, country_name = result["city"], result["country"]
        local_time = result["local_time"]
        current_weather = self.data_dict.get('current_weather', {})

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