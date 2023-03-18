import requests
from typing import Tuple
from geopy.geocoders import Nominatim
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