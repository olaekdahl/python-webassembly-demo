import requests

def fetch_data():
    response = requests.get("https://swapi.online/api/characters")
    data = response.json()
    return data