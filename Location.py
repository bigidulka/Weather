from typing import Tuple, Optional
from geopy.geocoders import Nominatim
import pytz
import datetime
from timezonefinder import TimezoneFinder
import requests


class Location:
    geolocator = Nominatim(user_agent="geoapiExercises")

    @staticmethod
    def get_coor_city(text: str) -> Optional[Tuple[float, float]]:
        location = Location.geolocator.geocode(text)
        return (location.latitude, location.longitude)
    
    @staticmethod
    def get_location_by_ip() -> Tuple[float, float]:
        response = requests.get('http://ip-api.com/json')
        data = response.json()
        return Location.get_coor_city(data['country'] + ' ' + data['city'])

    @staticmethod
    def get_name_time(coordinates: Tuple[float, float], language: str) -> dict:
        reverse = Location.geolocator.reverse
        location = reverse(
            f"{coordinates[0]}, {coordinates[1]}", language=language)

        return {
            "city": location.raw['address'].get('town') or location.raw['address'].get('city'),
            "country": location.raw['address'].get('country'),
            "local_time": datetime.datetime.now(pytz.timezone(TimezoneFinder().timezone_at(lng=coordinates[1], lat=coordinates[0]))),
        }
