import urllib.request, urllib.parse, urllib.error
import json

url = 'http://python-data.dr-chuck.net/comments_241040.json'
uh = urllib.request.urlopen(url)
data = uh.read()
js = json.loads(data)
# print json.dumps(js, indent=4)

print(sum([int(element['count']) for element in js['comments']]))
