# importera requests modulen för att jag kan använda API
import requests
import pandas as pd
# import piplot för att skapa olika typer av grafer och diagram, matlotlib är en bliblioteket
import matplotlib.pyplot as plt
import config

# Hämta apikey från config
apiKey = config.api_key

#Programmet kommer att fortsätta att köra så länge 'True' är sant. (När det t.ex kommer ett break eller exit, avslutas programmet)
while True:

    # Be användaren att skriva in stadsnamn
    cityInput = input('Ange stadsnamn och separerade dem med komma: ')

    # Skapa en lista, 'city' representerar varje stad i listan och strip() methoden ta bort extra mellanslag runt varje stad.
    # split(',') dela upp den i en lista av delsträngar vid varje kommatecken.
    cities = [city.strip() for city in cityInput.split(',')]

    # weatherList kommer att användas för att lagra väderinformation 'weatherData'
    weatherList = []

    # Loop som iterera över varje stad 'cities'
    for city in cities:
    # Om 'city' är tom, avsluta programmet
        if not city:
            print("Ingen stadsnamn. Avsluta programmet.")
            exit()

    # Skapa URL, hämta info med stadsnamnet och api-nyckeln
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}'
    # Gör en HTTP GET request till url
        response = requests.get(url)

    # Om vi får statuskod 200 OK
        if response.status_code == 200:
    # Konvertarar JSON svaret och omvandlar om temp från kelvin till celsius.
            data = response.json()
            temp_kelvin = data['main']['temp']
            temp_celsius = temp_kelvin - 273.15
            desc = data['weather'][0]['description']

    # Skapar ett dictionary 'weatherData' och lägger till den i 'weatherList'
            weatherData = {
                'City': city,
             'Temperature': temp_celsius,
                'Description': desc
            }
            weatherList.append(weatherData)

    # Om vi inte får statuskod 200 OK, skriv ett felmeddelande
        else:
            print('Error fetching weather data')

    # Skapa en Pandas DataFrame från 'weatherList'
    df = pd.DataFrame(weatherList)

    # Spara DataFrame som en csv-fil
    df.to_csv('weatherData.csv')

   #Kontrollera om kolumnen 'City' finns i weatherList
    if 'City' not in df.columns:
        print("Skriv rätt stadsnamn.")
    # Skapar ett stolpdiagram. X axeln = stadsnamn, Y axeln = temperature med diagrammet typen bar
    else:
        df.plot(x='City', y='Temperature', kind='bar')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature in Cities')

    # Visa diagrammet
    plt.show()

    # Skriv ut hela DataFrame till konsolen
    print(df)

#Om användaren skriver in fel stadsnamn, fråga om de vill köra programme igen eller avsluta.
    runAgain = input("Vill du köra programmet igen? (Ja / Nej): ").lower()
    if runAgain != 'ja':
        break