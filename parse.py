import requests
import json
from pprint import pprint
import itertools
import sqlite3
print("Lancement du script")

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
				vol_entier = ori + dest + heure_ar + heure_de
				vol_entier2.append(vol_entier)
# 				print vol_entier
				origine_air.append(ori)
				destination_air.append(dest)
# 				print origine_air
										
#print destination_air
#print count_vol
#print count_vol_connecting
#print vol_entier2
prix_vol_1 = price[0][3:7]
concatenate = zip(origine_air,destination_air)
#print concatenate

#initialisation bbd
connection = sqlite3.connect("travel.db")
cursor = connection.cursor()

#Tuple des valeurs recues
#vol1
vol_1_part_1 = concatenate[0][0]+concatenate[0][1]
vol_1_part_2 = concatenate[1][0]+concatenate[1][1]
prix_vol_1 = price[0][3:7]
vol_1 = [vol_1_part_1,vol_1_part_2,"",prix_vol_1]
trajet1=''.join(vol_1_part_1)
trajet2=''.join(vol_1_part_2)
trajet3=""
prix=''.join(prix_vol_1)
print vol_1
cursor.executemany('INSERT INTO orylax (trajet1, trajet2, trajet3, prix) values (?,?,?,?)',(vol_1,))
#vol2
vol_2_part_1 = concatenate[2][0]+concatenate[2][1]
vol_2_part_2 = concatenate[3][0]+concatenate[3][1]
vol_2_part_3 = concatenate[4][0]+concatenate[4][1]
prix_vol_2 = price[1][3:7]
if "LAX" in vol_2_part_3:
	vol_2 = [vol_2_part_1,vol_2_part_2,vol_2_part_3,prix_vol_2]
	cursor.executemany('INSERT INTO orylax (trajet1, trajet2, trajet3, prix) values (?,?,?,?)',(vol_2,))
else:
	vol_2 = [vol_2_part_1,vol_2_part_2,prix_vol_2]
#vol3
vol_3_part_1 = concatenate[5][0]+concatenate[5][1]
vol_3_part_2 = concatenate[6][0]+concatenate[6][1]
vol_3_part_3 = concatenate[7][0]+concatenate[7][1]
prix_vol_3 = price[1][3:7]
if "LAX" in vol_3_part_3:
        vol_3 = [vol_3_part_1,vol_3_part_2,vol_3_part_3,prix_vol_3]
else:
        vol_3 = [vol_3_part_1,vol_3_part_2,prix_vol_3]

vol = [(vol_1),(vol_2),(vol_3)]
#vol = zip(vol_1,vol_2,price)
print vol

#enregistrement
#file=open("result_vol_1","w")
#fichier=file.write(str(vol_1))
#file.close()

#test SQL
#connection = sqlite3.connect("travel.db")
#cursor = connection.cursor()
#var_string = ', '.join(map(str, vol_3))
#query = 'INSERT INTO orylax VALUES (?,?,?,?)'
#cursor.executemany(query, vol_3)
#cursor.executemany('INSERT INTO orylax (trajet1, trajet2, trajet3, prix) values (?,?,?,?)',(vol,))
connection.commit()
