import requests
import json
import sys
import sqlite3
import itertools

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

f = open("out.txt","w")
f.write(str(formatted_response))
#f.write(r)
f.close()

multivol = formatted_response['trips']['tripOption']
origine_air = []
destination_air = []
vol_entier = []
price = []
count_vol = 0
count_vol_connecting = 0
for p in multivol :
        multivol1 = p['slice']
        prix = p['saleTotal']
        price.append(prix)
        for q in multivol1 :
                count_vol += 1
                multivol2 = q['segment']
                duree_trip = q['duration']
                duree_trip_h = duree_trip // 60
                for s in multivol2 :
                        multivol3 = s['leg']
                        for d in multivol3 :
                                count_vol_connecting += 1
                                ori = d['origin']
                                dest = d['destination']
                                heure_ar = d['arrivalTime']
                                heure_de = d['departureTime']
                                vol_entier = ori + dest
#                               print vol_entier
                                origine_air.append(ori)
                                destination_air.append(dest)
#                               print origine_air

concatenate = zip(origine_air,destination_air)
#print concatenate
#sauvegarde des valeurs recues
vol_1_part_1 = concatenate[0][0]+concatenate[0][1]
vol_1_part_2 = concatenate[1][0]+concatenate[1][1]
prix_vol_1 = price[0][3:7]
vol_1 = [vol_1_part_1, vol_1_part_2,prix_vol_1]
print vol_1
vol_2_part_1 = concatenate[2][0]+concatenate[2][1]
vol_2_part_2 = concatenate[3][0]+concatenate[3][1]
prix_vol_2 = price[1][3:7]
vol_2 = [vol_2_part_1,vol_2_part_2,prix_vol_2]
print vol_2
vol = [(vol_1),(vol_2)]

#test SQL
connection = sqlite3.connect("travel.db")
cursor = connection.cursor()
#var_string = ', '.join(map(str, vol))
query = 'INSERT INTO orylax VALUES (?,?,?)'
cursor.executemany(query, vol)
connection.commit()
