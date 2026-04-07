import requests
#Kirjautuminen ei joistain syystä toiminut joten en saanut api avainta
city = input("Anna paikkakunta: ")
url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={""}")
response = requests.get(url)
data = response.json()
kelvin_temp = data["main"]["temp"]
celsius_temp = kelvin_temp - 273.15
description = data["weather"][0]["description"]
print(f"Sää: {description}")
print(f"Lämpötila: {celsius_temp:.1f} °C")