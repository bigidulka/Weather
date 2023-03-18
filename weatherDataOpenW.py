import requests


class WeatherDataOpenW:
    def __init__(self, coordinates, language) -> None:
        API_KEY = '666bd6866ee2225528565a3045a7a188'
        self.language = language
        latitude, longitude = coordinates

        self.__get_current_weather(API_KEY, latitude, longitude)
        self.__get_hourly_forecast(API_KEY, latitude, longitude)
        self.__get_daily_forecast(API_KEY, latitude, longitude)
        

    def __get_weather_data(self, url) -> None:
        params = {'lang': self.language}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return 'Error occurred while retrieving weather information.'

    def __get_current_weather(self, API_KEY, latitude, longitude) -> None:
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric'
        data = self.__get_weather_data(url)
        if type(data) == str:
            return data
        else:
            # Extract all data from the response JSON
            self.data_dict = {
                'temp': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'temp_min': data['main']['temp_min'],
                'temp_max': data['main']['temp_max'],
                'pressure': data['main']['pressure'],
                'humidity': data['main']['humidity'],
                'visibility': data['visibility'],
                'wind_speed': data['wind']['speed'],
                'wind_deg': data['wind']['deg'],
                'clouds': data['clouds']['all'],
                'sunrise': data['sys']['sunrise'],
                'sunset': data['sys']['sunset'],
                'country': data['sys']['country'],
                'name': data['name'],
                'weather_description': data['weather'][0]['description'],
                'weather_icon': data['weather'][0]['icon']
            }

    def __get_hourly_forecast(self, API_KEY, latitude, longitude) -> None:
        url = f'http://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric'
        data = self.__get_weather_data(url)
        if type(data) == str:
            return data
        else:
            self.hourly_forecast = []
            for forecast in data['list'][:48]:
                # Extract all data from the response JSON
                date = forecast['dt_txt']
                temp = forecast['main']['temp']
                feels_like = forecast['main']['feels_like']
                temp_min = forecast['main']['temp_min']
                temp_max = forecast['main']['temp_max']
                pressure = forecast['main']['pressure']
                humidity = forecast['main']['humidity']
                visibility = forecast.get('visibility')
                wind_speed = forecast['wind']['speed']
                wind_deg = forecast['wind']['deg']
                clouds = forecast['clouds']['all']
                weather_description = forecast['weather'][0]['description']
                weather_icon = forecast['weather'][0]['icon']

            # Append a dictionary containing all the variables to the hourly_forecast list
            self.hourly_forecast.append({
                'date': date,
                'temp': temp,
                'feels_like': feels_like,
                'temp_min': temp_min,
                'temp_max': temp_max,
                'pressure': pressure,
                'humidity': humidity,
                'visibility': visibility,
                'wind_speed': wind_speed,
                'wind_deg': wind_deg,
                'clouds': clouds,
                'weather_description': weather_description,
                'weather_icon': weather_icon
            })

    def __get_daily_forecast(self, API_KEY, latitude, longitude) -> None:
        url = f'http://api.openweathermap.org/data/2.5/forecast/daily?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric&cnt=8'
        data = self.__get_weather_data(url)
        if type(data) == str:
            return data
        else:
            self.daily_forecast = []
            for forecast in data['list']:
                # Extract all data from the response JSON
                date = forecast['dt']
                temp = forecast['temp']['day']
                feels_like_day = forecast['feels_like']['day']
                feels_like_night = forecast['feels_like']['night']
                temp_min = forecast['temp']['min']
                temp_max = forecast['temp']['max']
                pressure = forecast['pressure']
                humidity = forecast['humidity']
                wind_speed = forecast['speed']
                wind_deg = forecast['deg']
                clouds = forecast['clouds']
                weather_description = forecast['weather'][0]['description']
                weather_icon = forecast['weather'][0]['icon']

            # Append a dictionary containing all the variables to the daily_forecast list
            self.daily_forecast.append({
                'date': date,
                'temp': temp,
                'feels_like_day': feels_like_day,
                'feels_like_night': feels_like_night,
                'temp_min': temp_min,
                'temp_max': temp_max,
                'pressure': pressure,
                'humidity': humidity,
                'wind_speed': wind_speed,
                'wind_deg': wind_deg,
                'clouds': clouds,
                'weather_description': weather_description,
                'weather_icon': weather_icon
            })