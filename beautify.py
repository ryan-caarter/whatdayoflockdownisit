import bs4
import os
import sys

folder_path = "." if len(sys.argv) == 1 else sys.argv[1]
for filename in os.listdir(folder_path):
    if filename.endswith('.html'):
        with open(os.path.join(folder_path, filename), "r") as file:
            soup = bs4.BeautifulSoup(file.read(), 'html.parser')

            # if this brandong tag doesn't exist clean has already happened
            tag = soup.select_one('a[style*="flex: 1 1; height: 3rem; padding-left: 1rem;"]')
            if tag is None:
                print("You've already cleaned "+filename)
            else:
                # hide it by setting height 0
                tag['style'] = "flex: 1 1; height: 0; padding-left: 1rem;"
                print("Cleaning " + filename)

            # remove annoying meta tag
            tag = soup.select_one('meta[name*="generator"]')
            if tag is not None:
                tag.extract()

            # fix links that link to itself
            soup = bs4.BeautifulSoup(str(soup).replace(filename, "#"), 'html.parser')

            # remove mobirise comments, add our auth tag
            # for comment in soup.find_all(text=lambda e: isinstance(e, bs4.Comment)):
            #     comment.extract()
            # comment = bs4.Comment("\nsite by Ryan Carter & Lucas Quennell\nryan.c4rter@gmail.com\nlucasryanq@gmail.com")
            # soup.head.insert(0, comment)

            # remove other branding tag
            [el.extract() for el in soup.select("[style='flex: 0 0 auto; margin:0; padding-right:1rem;']")]
            file.close()
            file = open(os.path.join(folder_path, filename), "w", encoding='utf-8')

            # make it pretty
            file.write(str(soup.prettify()))
            file.close()
print("Done! ")
