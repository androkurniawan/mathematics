import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/feed/storefront?bp=ogUCKAU%3D"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Mengambil semua tag h2
h2_tags = soup.find_all("h2")

for i, h2 in enumerate(h2_tags, start=1):
    print(f"H2 ke-{i}: {h2.text.strip()}")