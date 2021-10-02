import bs4
import os
import sys
import requests

folder_path = "." if len(sys.argv) == 1 else sys.argv[1]
for filename in os.listdir(folder_path):
    if filename.endswith('.html'):
        with open(filename, "r") as file:
            soup = bs4.BeautifulSoup(file.read(), 'html.parser')
            file.close()
            tag = int(soup.find("h1", {"id": "answer_lockdown"}).string.strip()) + 1
            soup.find("h1", {"id": "answer_lockdown"}).string = str(tag)

            URL = "https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-current-cases"
            page = requests.get(URL)
            soup2 = bs4.BeautifulSoup(page.content, 'html.parser')
            tags = soup2.find_all("table", class_="table-style-two")[0]
            cases = tags.find("strong").string

            soup.find("h1", {"id": "answer_cases"}).string = cases
            file = open(os.path.join(folder_path, filename), "w", encoding='utf-8')

            # make it pretty
            file.write(str(soup.prettify()))
            file.close()

print("Updated site and cleaned!")
