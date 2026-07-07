import requests
from bs4 import BeautifulSoup

url = "https://siakad.iteba.ac.id/dosen/dashboard"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

i = 1
for quote in quotes:
    author = quote.find("small", class_="author").text

    if author == "Albert Einstein":
        text = quote.find("span", class_="text").text
        # print(text)
        print(f"{i}. {text}")
        i += 1