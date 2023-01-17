from yaweather import cities
import geocoder
import requests

class Location:
    @classmethod
    def countries(cls):
        return sorted([c.name() for c in cities.CountryBase.__subclasses__()])
    
    @classmethod
    def cities(cls, country):
        country_class = getattr(cities, country)
        cities_ = dict(sorted(country_class.cities().items()))
        return cities_.keys()
    
    @classmethod
    def get_coordinates_city(cls, country, city):
        country_class = getattr(cities, country)
        return country_class.cities()[city]

    @classmethod
    def getIP(cls):
        return requests.get('https://api.ipify.org').text

    @classmethod
    def getLocation(cls):
        geo = geocoder.ip(cls.getIP())
        return geo.city, geo.country, geo.latlng