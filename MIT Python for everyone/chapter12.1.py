import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url_sample = 'http://python-data.dr-chuck.net/comments_42.html'
url_actual = 'http://python-data.dr-chuck.net/comments_241039.html'
html = urllib.request.urlopen(url_actual).read()
soup = BeautifulSoup(html, "lxml")

print(sum([int(tag.contents[0]) for tag in soup.find_all('span')]))
