from bs4 import BeautifulSoup
import requests
import smtplib
import os

my_email = "dianageorgievasvishtov@gmail.com"
password = os.environ["PASSWORD"]

product_url = "https://www.amazon.de/-/en/dp/B07YLZKLKQ/?coliid=I2GPRWDUH0MAIW&colid=3FWMQAEHKJZKF&ref_=lv_ov_lig_dp_it_im&th=1&psc=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,bg;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "cross-site"
}

response = requests.get(url=product_url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

price_tag = soup.find(name="span", class_="a-offscreen")
price_string = price_tag.getText()
product_price = float(price_string.split("€")[1])
product_tag = soup.find(name="span", id="productTitle")
product_name = product_tag.getText()

if product_price < 100:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="dianageorgievasvishtov@yahoo.com", msg=
                        str(f"Subject:Hot price\n\n"
                            f"Hello darling,"
                            f"\n{product_name} is now at price €{product_price}.\nLINK: {product_url}").encode('utf-8'))




