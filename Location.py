from yaweather import cities
import requests
from typing import Tuple
from geopy.geocoders import Nominatim

class Location:
    @classmethod
    def get_info_city(cls, city_and_country) -> Tuple[Tuple[float, float], dict[str, str]]:
        geolocator = Nominatim(user_agent="geoapiExercises")

        location = geolocator.geocode(city_and_country)

        if location is None:
            return
        else:
           return (location.latitude, location.longitude), {location.address.split(',')[0]: location.address.split(',')[-1]}
    
    @classmethod
    def get_countries(cls):
        return sorted([c.name() for c in cities.CountryBase.__subclasses__()])
    
    @classmethod
    def get_cities(cls, country):
        country_class = getattr(cities, country)
        cities_ = dict(sorted(country_class.cities().items()))
        return cities_.keys()

    @classmethod
    def getIP(cls) -> str:
        return requests.get('https://api.ipify.org').text
    
    @classmethod
    def add_city(cls, country: str, city_name: str, latitude: float, longitude: float):
        country_class = getattr(cities, country)
        setattr(country_class, city_name, (latitude, longitude))
    
    @classmethod
    def get_location_by_ip(cls) -> Tuple[Tuple[float, float], dict[str, str]]:
        response = requests.get('http://ip-api.com/json')
        data = response.json()
        return (data['lat'], data['lon']), dict(country=data['country'], city=data['city'])