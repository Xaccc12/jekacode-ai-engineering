import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 6.5244,     # Lagos
    "longitude": 3.3792,
    "current_weather": True,
}

response = requests.get(url, params=params)
data = response.json()      # JSON text → Python dict

print(data["current_weather"])