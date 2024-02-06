import requests
import pandas as pd
import matplotlib.pyplot as plt
import config

api_key = config.api_key

city_input = input('Enter city names (comma-separated): ')

cities = [city.strip() for city in city_input.split(',')]

weatherList = []

for city in cities:

    if not city:
        continue

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url)

