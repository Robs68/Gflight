#!/home/root/bin/python
import requests
import json
import sys
import sqlite3
import itertools
import argparse
import time

#origin = "ORY"
#destination = "LHR"
#date = "2017-09-20" Y-M-D
temps = time.strftime('%H:%M')
print temps
print "lancement du script python orylax"
#arguments en IN
parser = argparse.ArgumentParser()
parser.add_argument('-o',dest='origin')
parser.add_argument('-d',dest='destination')
parser.add_argument('-date',dest='date')
args = parser.parse_args()

#passage en minuscule pour bdd
origine = args.origin
destination = args.destination
date = args.date

origine = origine.lower()
destination = destination.lower()
name_of_bdd = ''.join((origine,destination))

payload = {
  "request": {
    "passengers": {
      "adultCount": "1"
    },
    "slice": [
      {
        "origin": args.origin,
        "destination": args.destination,
        "date": args.date
      }
    ],
    "solutions": "5"
  }
}

url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyC9POMBiqyNxkigQG9rBguzKDlvZU0BcAM'
r = requests.post(url, json=payload)
formatted_response = r.json()
test_response = r.json()

#Save fichier
#f = open("out.txt","w")
#f.write(str(formatted_response))
#f.write(r)
#f.close()

#f = open("out3.txt","w")
#f.write(str(formatted_response))
#f.write(r)
#f.close()

multivol = formatted_response['trips']['tripOption']
origine_air = []
destination_air = []
vol_entier = []
price = []
vol_entier2 = []
count_vol = 0
count_vol_connecting = 0
for p in multivol :
#	print("")
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
				vol_entier = ori + dest + heure_de + heure_ar
				vol_entier2.append(vol_entier)
# 				print vol_entier
				origine_air.append(ori)
				destination_air.append(dest)
# 				print origine_air
										
concatenate = zip(origine_air,destination_air)

#initialisation bbd
connection = sqlite3.connect("travel.db")
cursor = connection.cursor()

#date
now = time.strftime('%Y-%m-%d-T-%H:%M')
#Tuple des valeurs recues
#print vol_entier2
#vol1
vol_1_part_1 = concatenate[0][0]+concatenate[0][1]
prix_vol_1 = price[0][3:7]
if args.destination in vol_1_part_1:
	vol_1 = [now,vol_1_part_1," "," ", heure_de,duree_trip,prix_vol_1]
else:
	vol_1_part_2 = concatenate[1][0]+concatenate[1][1]
	if args.destination in vol_1_part_2:
		vol_1 = [now,vol_1_part_1,vol_1_part_2," ",heure_de,duree_trip,prix_vol_1]
	else:
		vol_1_part_3 = concatenate[2][0]+concatenate[2][1]
		vol_1 = [now,vol_1_part_1,vol_1_part_2,vol_1_part_3,heure_de,duree_trip,prix_vol_1]

cursor.executemany('INSERT INTO orylax (heure_recherche,trajet1, trajet2, trajet3, heure_depart, duree, prix) values (?,?,?,?,?,?,?)',(vol_1,))
#cursor.executrmany('delete from orylax where rowid not in (select min(rowid) from orylax group by heure_depart,prix)')
connection.commit()
print ("script fini")
