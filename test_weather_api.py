import requests

api_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&temperature_unit=fahrenheit"
response = requests.get(api_url)

print(response.json())


