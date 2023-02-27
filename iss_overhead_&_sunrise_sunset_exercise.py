import requests
from datetime import datetime


response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
response.raise_for_status()
data = response.json()
# print(data)
iss_longitude = data["iss_position"]["longitude"]  
iss_latitude = data["iss_position"]["latitude"]


# Sunrise and sunset exercise.

MY_LAT = 46.671295  # Your latitude
MY_LONG = 11.152518  # Your longitude

parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now().hour


