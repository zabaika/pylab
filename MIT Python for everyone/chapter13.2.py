import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'sensor': 'false', 'address': address})
    # print 'Retrieving', url
    uh = urllib.request.urlopen(url)
    data = uh.read()
    # print 'Retrieved',len(data),'characters'

    try:
        js = json.loads(str(data))
    except:
        js = None
    if 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print json.dumps(js, indent=4)
    for i in range(len(js['results'])):
        print(js["results"][i]["place_id"])
