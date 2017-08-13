import requests
import json
import sys

#origin = input("What is your city of origin? (Three letters):    ")
#destination = input("Where would you like to travel to? (Three letters):    ")
#date = input("What day would you like to fly there? One way flights only right now. (YYYY-MM-DD):    ")

payload = {
  "request": {
    "passengers": {
      "adultCount": "1"
    },
    "slice": [
      {
        "origin": "ORY",
        "destination": "LAX",
        "date": "2017-09-10"
      }
    ],
    "solutions": "20"
  }
}

url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyC9POMBiqyNxkigQG9rBguzKDlvZU0BcAM'
r = requests.post(url, json=payload)
formatted_response = r.json()
total = formatted_response["trips"]["tripOption"][0]["saleTotal"] 

print("Total:", total)
test_response = r.json()


#print(test_response)
airport_list = formatted_response["trips"]["data"]["airport"]

print("") 
for trip in formatted_response["trips"]["tripOption"]:
	for slices in trip["slice"]:
		for segment in slices["segment"]:
			for leg in segment["leg"]:
				for airport in airport_list:
					airport_o = formatted_response["trips"]["tripOption"][0]["slice"][0]["segment"][0]["leg"][0]["origin"]
					airport_d = formatted_response["trips"]["tripOption"][0]["slice"][0]["segment"][0]["leg"][0]["destination"]
					duration = formatted_response["trips"]["tripOption"][0]["slice"][0]["segment"][0]["leg"][0]["duration"]
#change = formatted_response["trips"]["tripOption"][0]["slice"][0]["segment"][0]["leg"][0]["changePlane"]
print("airport origin:", airport_o, "airport destination", airport_d, "duree", duration)

f = open("out.txt","w")
f.write(str(formatted_response))
#f.write(r)
f.close()

multivol = formatted_response['trips']['tripOption']
for p in multivol :
        multivol1 = p['slice']
        prix = p['saleTotal']
        print prix
        for q in multivol1 :
                multivol2 = q['segment']
                durra = q['duration']
                print durra
                for s in multivol2 :
                        multivol3 = s['leg']
                        for d in multivol3 :
                                ori = d['origin']
                                dest = d['destination']
                                vola = ori + dest
                                print vola
