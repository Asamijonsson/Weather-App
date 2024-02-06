import requests
import pandas as pd
import matplotlib.pyplot as plt

api_key = "56ae12255c16f1343f4b7dcf3d2a9871"

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url)