from yaweather import cities
import geocoder
import requests

class Location:
    
    @classmethod
    def get_countries(cls):
        return sorted([c.name() for c in cities.CountryBase.__subclasses__()])
    
    @classmethod
    def get_cities(cls, country):
        country_class = getattr(cities, country)
        cities_ = dict(sorted(country_class.cities().items()))
        return cities_.keys()

    @classmethod
    def getIP(cls):
        return requests.get('https://api.ipify.org').text

    @classmethod
    def getLocation(cls):
        geo = geocoder.ip(cls.getIP())
        return geo.city, geo.country, geo.latlng
    
    @classmethod
    def add_city(cls, country, city_name: str, latitude: float, longitude: float):
        country_class = getattr(cities, country)
        setattr(country_class, city_name, (latitude, longitude))
        
Location.add_city("Russia", "Voskresensk", 55.3173, 38.6526)