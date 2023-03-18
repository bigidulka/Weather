import requests


class WeatherDataWAPI:
    def __init__(self, coordinates, language) -> None:
        API_KEY = '487da948423c4322b24221408231703'
        self.language = language
        self.latitude, self.longitude = coordinates

        self.__get_current_weather(API_KEY)
        # self.__get_hourly_forecast(API_KEY, latitude, longitude)
        # self.__get_daily_forecast(API_KEY, latitude, longitude)
        

    def __get_weather_data(self, url) -> None:
        params = {'lang': self.language, 'q': f'{self.latitude},{self.longitude}'}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            print(data)
            return data
        else:
            return 'Error occurred while retrieving weather information.'

    def __get_current_weather(self, API_KEY) -> None:
        url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&units=metric'
        data = self.__get_weather_data(url)
        if type(data) == str:
            return data
        else:
            # Extract all data from the response JSON
            self.data_dict = {
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
     
    def __get_hourly_forecast(self, API_KEY, latitude, longitude) -> None:
        # url = f'http://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric'
        # data = self.__get_weather_data(url)
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
        # url = f'http://api.openweathermap.org/data/2.5/forecast/daily?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric&cnt=8'
        # data = self.__get_weather_data(url)
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