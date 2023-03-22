import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 42.611461
MY_LONG = 23.371008
my_email = "dianageorgievasvishtov@gmail.com"
my_password = "cnhuskjvbggzvvtw"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Position is within +5 or -5 degrees of the ISS position.
def iss_overhead():
    if iss_latitude + 5 >= MY_LAT >= iss_latitude - 5 and iss_longitude + 5 >= MY_LONG >= iss_longitude - 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = int(time_now.hour)

while True:
    time.sleep(60)
    if iss_overhead() and sunrise > hour_now or hour_now > sunset:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="dianageorgievasvishtov@yahoo.com",
                                msg="Subject:ISS is here \n\n"
                                    "ISS is right now above you and you can see it once dark")
