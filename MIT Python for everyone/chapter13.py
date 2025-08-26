import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_241036.xml'
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

results = tree.findall('.//count')  # https://docs.python.org/2/library/xml.etree.elementtree.html#elementtree-xpath
print(sum([int(count.text) for count in results]))
