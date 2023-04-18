from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
site_content = response.text
soup = BeautifulSoup(site_content, "html.parser")
film_tag = soup.find_all(name="h3", class_="title")
film_list = [tag.getText() for tag in film_tag]

# film_list = []
# for tag in film_tag:
#     film_content = tag.getText()
#     film_list.append(film_content)
new_list = film_list[::-1]

with open(file="movies.txt", mode="w", encoding="utf-8") as file:
    for item in new_list:
        file.write(f"{item}\n")





