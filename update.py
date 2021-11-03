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
    first_dose = tags[0].string
    second_dose = tags[1].string
    new_cases = tags[3].string
    active_cases = tags[4].string
    soup.find("h1", {"id": "answer_new_cases"}).string = new_cases
    soup.find("h1", {"id": "answer_active_cases"}).string = active_cases
    soup.find("h1", {"id": "answer_first_vaccine"}).string = first_dose
    soup.find("h1", {"id": "answer_second_vaccine"}).string = second_dose

file = open("index.html", "r")
soup = bs4.BeautifulSoup(file.read(), 'html.parser')
file.close()

if len(sys.argv) > 1:
    if sys.argv[1] == "1":
        print("Days selected ⏱  Updating..")
        update_day_count(soup)
    elif sys.argv[1] == "2":
        print("Cases selected 💼 Updating..")
        update_cases_and_vaccines(soup)
    elif sys.argv[1] == "3":
        print("Days and cases selected ⏱💼 Updating..")
        update_cases_and_vaccines(soup)
        update_day_count(soup)
    print("Updated site 💯💯")
else:
    print("Pick an option.")

file = open("index.html", "w", encoding='utf-8')

file.write(str(soup.prettify()))
file.close()
