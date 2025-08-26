import urllib
import re
from bs4 import BeautifulSoup

url = 'http://python-data.dr-chuck.net/known_by_Nyree.html'
counts = 7
position = 18
names = [re.findall('by_(.+).html', url)]

for i in range(counts):
    print 'Retrieving:', url
    soup = BeautifulSoup(urllib.urlopen(url).read(), "lxml")
    url = soup.find_all('a')[position-1].get('href')
    names.append(re.findall('by_(.+).html', url))
print names.pop()
