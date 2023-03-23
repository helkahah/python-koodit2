import json
import requests

hakusana = input("Anna paikkakunnan nimi: ")

pyyntö = "https://api.openweathermap.org/data/2.5/weather?q=" + hakusana + \
         "&units=metric&lang=fi&appid=f26e539d38ff2bf99b3737dac9ad3a6e"

print("tässä on hakulause:")
print(pyyntö)

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(f"{hakusana} sää: "
              f"{json_vastaus['main']['temp']}°C, "
              f"{json_vastaus['weather'][0]['description']}")


except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")