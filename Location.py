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
    def get_name_time(coordinates: Tuple[float, float], language: str) -> dict:
        geolocator = Nominatim(user_agent="geoapiExercises")
        reverse = geolocator.reverse
        location = reverse(
            f"{coordinates[0]}, {coordinates[1]}", language=language)

        return {
            "city": location.raw['address'].get('town') or location.raw['address'].get('city'),
            "country": location.raw['address'].get('country'),
            "local_time": datetime.datetime.now(pytz.timezone(TimezoneFinder().timezone_at(lng=coordinates[1], lat=coordinates[0]))),
        }
