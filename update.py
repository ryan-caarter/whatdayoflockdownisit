import bs4
import os
import sys
import requests

def update_day_count(soup):
    tag = int(soup.find("h1", {"id": "answer_lockdown"}).string.strip()) + 1
    soup.find("h1", {"id": "answer_lockdown"}).string = str(tag)

def update_cases(soup):
    URL = "https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-current-cases"
    page = requests.get(URL)
    soup2 = bs4.BeautifulSoup(page.content, 'html.parser')
    tags = soup2.find_all("table", class_="table-style-two")[0]
    cases = tags.find("strong").string
    soup.find("h1", {"id": "answer_cases"}).string = cases


file = open("index.html", "r")
soup = bs4.BeautifulSoup(file.read(), 'html.parser')
file.close()

if len(sys.argv) == 1:
    print("Days selected  ⏱ Updating..")
    update_day_count(soup)
else:
    update_cases(soup)
    print("Cases selected 🧳 Updating..")

file = open("index.html", "w", encoding='utf-8')

file.write(str(soup.prettify()))
file.close()
print("Updated site 💯")
