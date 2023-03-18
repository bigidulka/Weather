from weatherDataOpenW import WeatherDataOpenW

class Translate:
    def __init__(self, Time: str, weather_data: WeatherDataOpenW) -> None:
        self.Time = Time
        self.weather_data = weather_data
        
    def get_translation(self) -> dict:
        language = self.weather_data.language
        if language == 'en':
            translation = {
                'nameCityCountry': f"{self.weather_data.data_dict.get('location', {}).get('name', '')}, {self.weather_data.data_dict.get('location', {}).get('country', '')}",
                'time': f"It is now {self.weather_data.data_dict.get('location', {}).get('localtime', '')}. Yesterday at this time {0}",
                'temp': self.weather_data.data_dict.get('temp_c', ''),
                'condition': self.weather_data.data_dict.get('condition:text', ''),
                'feels_like': f"Feels like {self.weather_data.data_dict.get('feelslike_c', '')}"
            }
        elif language == 'ru':
            translation = {
                'nameCityCountry': f"{self.weather_data.data_dict.get('location', {}).get('name', '')}, {self.weather_data.data_dict.get('location', {}).get('country', '')}",
                'time': f"Сейчас {self.weather_data.data_dict.get('location', {}).get('localtime', '')}. Вчера в это время было {0}",
                'temp': self.weather_data.data_dict.get('temp', ''),
                'condition': self.weather_data.data_dict.get('weather_description', ''),
                'feels_like': f"Ощущается как {self.weather_data.data_dict.get('feels_like', '')}"
            }
        else:
            raise ValueError(f"Unsupported language: {language}")
        return translation