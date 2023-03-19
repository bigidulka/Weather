import requests
from typing import Tuple
from geopy.geocoders import Nominatim
from functools import partial
import pytz
import datetime
from timezonefinder import TimezoneFinder


class Location:
    @staticmethod
    def get_coor_city(text: str) -> Tuple[float, float]:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(text)
        return (location.latitude, location.longitude)

    @staticmethod
    def get_location_by_ip() -> Tuple[float, float]:
        response = requests.get('http://ip-api.com/json')
        data = response.json()
        return Location.get_coor_city(data['country'] + ' ' + data['city'])

    @staticmethod
    def get_name_time(coordinates: Tuple[float, float], language: str) -> dict:
        geolocator = Nominatim(user_agent="geoapiExercises")
        reverse = partial(geolocator.reverse, language=language)
        location = reverse(f"{coordinates[0]}, {coordinates[1]}")

        return {
            "city": location.raw['address'].get('town') or location.raw['address'].get('city'),
            "country": location.raw['address'].get('country'),
            "local_time": datetime.datetime.now(pytz.timezone(TimezoneFinder().timezone_at(lng=coordinates[1], lat=coordinates[0])))
        }
