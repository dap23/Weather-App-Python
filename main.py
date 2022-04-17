import requests

API_KEY = "<Your API KEY>"
URI = "http://api.openweathermap.org/data/2.5/weather"

city = input("Masukan nama kota: ")
req_url = f"{URI}?appid={API_KEY}&q={city}"
res = requests.get(req_url)

if res.status_code == 200:
    data = res.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "Celsius")
else:
    print("An error occured")
