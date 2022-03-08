"""This module parses internet page and writes words into file"""
from bs4 import BeautifulSoup
import requests

url = "https://slotobzor.com/nastolnye-igry-dlya-vzroslyh/slozhnye-slova-dlya-ugadyvaniya-na-igru-viselitsa-interesnye-primery/"

r = requests.get(url)

soup = BeautifulSoup(r.text, features="html.parser")
div = soup.find('div', class_="entry-content")
li = div.findAll('li', class_="")

with open("words.txt", "w") as file:
    for elem in li:
        file.write(str(elem)[4:-5] + "\n")
