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

    if response.status_code == 200:
        data = response.json()
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        desc = data['weather'][0]['description']

        weatherData = {
            'City': city,
         'Temperature': temp_celsius,
            'Description': desc
        }
        weatherList.append(weatherData)

    else:
        print('Error fetching weather data')

df = pd.DataFrame(weatherList)

# Save DataFrame to a CSV file
df.to_csv('weatherData.csv', index=False)

df.plot(x='City', y='Temperature', kind='bar', legend=False)
plt.ylabel('Temperature (°C)')
plt.title('Temperature in Cities')
plt.show()

# Display the DataFrame
print(df)