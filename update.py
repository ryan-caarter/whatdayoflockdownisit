import bs4
import os
import sys
import requests

def update_day_count(soup):
    tag = int(soup.find("h1", {"id": "answer_lockdown"}).string.strip()) + 1
    soup.find("h1", {"id": "answer_lockdown"}).string = str(tag)

def update_cases_and_vaccines(soup):
    URL = "https://covid19.govt.nz/"
    page = requests.get(URL)
    soup2 = bs4.BeautifulSoup(page.content, 'html.parser')
    tags = soup2.find_all("p", class_="number__value")
    new_cases = tags[0].string
    active_cases = tags[1].string
    first_dose = tags[2].string
    second_dose = tags[3].string
    soup.find("h1", {"id": "answer_new_cases"}).string = new_cases
    soup.find("h1", {"id": "answer_active_cases"}).string = active_cases
    soup.find("h1", {"id": "answer_first_vaccine"}).string = str(round(int(first_dose.replace(",",""))/5000000 * 100,2)) + "%"
    soup.find("h1", {"id": "answer_second_vaccine"}).string = str(round(int(second_dose.replace(",",""))/5000000 * 100,2)) + "%"

file = open("index.html", "r")
soup = bs4.BeautifulSoup(file.read(), 'html.parser')
file.close()

if len(sys.argv) == 1:
    print("Days selected ⏱ Updating..")
    update_day_count(soup)
else:
    update_cases_and_vaccines(soup)
    print("Cases selected 🧳 Updating..")

file = open("index.html", "w", encoding='utf-8')

file.write(str(soup.prettify()))
file.close()
print("Updated site 💯💯")
