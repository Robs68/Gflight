import urllib2
import json
import requests

api_key = "AIzaSyC9POMBiqyNxkigQG9rBguzKDlvZU0BcAM"
url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
headers = {'content-type': 'application/json'}

params = {
  "request": {
    "slice": [
      {
        "origin": "ORY",
        "destination": "LAX",
        "date": "2017-09-10"
      }
    ],
    "passengers": {
      "adultCount": 1
    },
    "solutions": 2,
    "refundable": False
  }
}

jsonreq = json.dumps(params, encoding = 'utf-8')
req = urllib2.Request(url, jsonreq, {'Content-Type': 'application/json'})
flight = urllib2.urlopen(req)
response = flight.read()
flight.close()
#print(response)

#f = open("out2","w")
#f.write(response)
#f.close()
