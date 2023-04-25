import requests

url = 'http://api.weatherapi.com/v1/current.json?key=487da948423c4322b24221408231703&q=москва'
with requests.Session() as session:
    response = session.get(url)
    response.raise_for_status()
    print(response.json())