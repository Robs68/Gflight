import requests
import json
from pprint import pprint
import itertools
import sqlite3
print("Lancement du script ORYLAX pour le 2017-09_10")

file = open("out3", "r")
fichier=file.read()
with open('out3') as data_file:
	data = json.load(data_file)

#mutlievols
multivol = data['trips']['tripOption']
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

#Tuple des valeurs recues
#print vol_entier2
#vol1
vol_1_part_1 = concatenate[0][0]+concatenate[0][1]
prix_vol_1 = price[0][3:6]
if "LAX" in vol_1_part_1:
	vol_1 = [vol_1_part_1," "," ", heure_de,duree_trip,prix_vol_1]
else:
	vol_1_part_2 = concatenate[1][0]+concatenate[1][1]
	if "LAX" in vol_1_part_2:
		vol_1 = [vol_1_part_1,vol_1_part_2," ",heure_de,duree_trip,prix_vol_1]
	else:
		vol_1_part_2 = concatenate[2][0]+concatenate[2][1]
		vol_1 = [vol_1_part_1,vol_1_part_2,vol_1_part_3,heure_de,duree_trip,prix_vol_1]

cursor.executemany('INSERT INTO orylax (trajet1, trajet2, trajet3, heure_depart, duree, prix) values (?,?,?,?,?,?)',(vol_1,))
connection.commit()
print ("script fini")
