from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

city_and_country = input("Enter the name of the city and country: ")

location = geolocator.geocode(city_and_country)

print("Latitude: ", location.latitude)
print("Longitude: ", location.longitude)
print("City: ", location.address.split(',')[0])
print("Country: ", location.address.split(',')[-1])