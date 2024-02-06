import requests
import pandas as pd
import matplotlib.pyplot as plt

api_key = "56ae12255c16f1343f4b7dcf3d2a9871"

city_input = input('Enter city names (comma-separated): ')

cities = [city.strip() for city in city_input.split(',')]

weatherList = []

for city in cities:

    if not city:
        continue

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url)

