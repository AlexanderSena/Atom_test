from bs4 import BeautifulSoup
import requests

source = requests.get('https://space.skyrocket.de/doc_chr/lau2018.htm').text

#base = source.content

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('a'):
    headline = article.text
    print(headline)
    print()
