from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException



# SCRAPING RENTAL DATA FROM ZILLOW
google_form = "https://forms.gle/Hi5JApCtZNwwnQAr5"
zillow_link = "https://www.zillow.com/homes/for_rent/1-_beds/?" \
              "searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%" \
              "2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%" \
              "3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%" \
              "2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%" \
              "3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%" \
              "3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%" \
              "22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%" \
              "3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%" \
              "22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,bg;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "cross-site"
}
response = requests.get(url=zillow_link, headers=header)
soup = BeautifulSoup(response.content, "html.parser")
addresses = soup.find_all(name="address")
addresses_list = [address.getText() for address in addresses]


prices = soup.find_all("span", attrs={"data-test": "property-card-price"})
prices_list = [price.getText() for price in prices]

links = soup.find_all("a", href=True, attrs={"tabindex": "-1"}, class_="property-card-link")
links_list = [link["href"] for link in links]
new_links_list = []
for item in links_list:
    if item[0] == "/":
        new_item = f"https://www.zillow.com{item}"
        new_links_list.append(new_item)
    else:
        new_links_list.append(item)


# POPULATING DATA IN FORM
service = Service(r"C:\Users\diana\PycharmProjects\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get(google_form)
driver.implicitly_wait(5)

for n in range(len(addresses_list)):
    address_to_input = addresses_list[n]
    price_to_input = prices_list[n]
    link_to_input = new_links_list[n]
    print(f"{address_to_input}, {price_to_input}, {link_to_input}")
    try:
        input_address = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        input_address.send_keys(address_to_input)
    except ElementNotInteractableException:
        pass
    finally:
        driver.implicitly_wait(5)
        input_price = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        input_price.send_keys(price_to_input)
        driver.implicitly_wait(5)
        input_link = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        input_link.send_keys(link_to_input)
        driver.implicitly_wait(5)
        send_button = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
        send_button.click()
        driver.implicitly_wait(5)
        new_form = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        new_form.click()
driver.close()

# GET RESPONSES FILE (wip)
# driver.get("https://docs.google.com/forms/d/1lgbqoedXm2jKmVfiCMKCOvnT4bCk8fc5lQ7NWaTaGOI/edit?pli=1#responses")
# time.sleep(10)
# driver.switch_to.frame("Qr4Z0d")
# driver.implicitly_wait(10)
# style_button = driver.find_element(By.XPATH, "//*[@id='inproduct-guide-modal']/div[3]/button")
# style_button.click()
# driver.implicitly_wait(5)
# results = driver.find_element(By.CSS_SELECTOR, "span .NPEfkd RveJvd snByac")
# results.click()
