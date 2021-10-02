import bs4
import os
import sys
from git import Repo

folder_path = "." if len(sys.argv) == 1 else sys.argv[1]
for filename in os.listdir(folder_path):
    if filename.endswith('.html'):
        with open(filename, "r") as file:
            soup = bs4.BeautifulSoup(file.read(), 'html.parser')
            file.close()
            tag = int(soup.find("h1", {"id": "answer"}).string.strip()) + 1
            soup.find("h1", {"id": "answer"}).string = str(tag)
            comment = bs4.Comment("\nsite by Ryan Carter\nryan.c4rter@gmail.com")
            soup.head.insert(0, comment)

            file = open(os.path.join(folder_path, filename), "w", encoding='utf-8')

            # make it pretty
            file.write(str(soup.prettify()))
            file.close()
