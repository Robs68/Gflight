import requests
import json
from pprint import pprint
import itertools
import sqlite3
print("Lancement du script")

file = open("out2", "r")
fichier=file.read()
with open('out2') as data_file:
	data = json.load(data_file)

#mutlievols
multivol = data['trips']['tripOption']
origine_air = []
destination_air = []
vol_entier = []
price = []
count_vol = 0
count_vol_connecting = 0
for p in multivol :
	print("")
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
#				print vol_entier
				origine_air.append(ori)
				destination_air.append(dest)
#				print origine_air
										
#print destination_air
print count_vol
print count_vol_connecting
titi = []
for i in range(0,len(origine_air)):
	origine = origine_air[i][0:3] #trouve les 3 premier caracteres
	destination = origine_air[i][3:6]
	titi.append(origine)
	titi.append(destination)
print("")
#print titi[0]
#print titi[1]
prix_vol_1 = price[0][3:7]
concatenate = zip(origine_air,destination_air)
#print concatenate
#sauvegarde des valeurs recues
vol_1_part_1 = concatenate[0][0]+concatenate[0][1]
vol_1_part_2 = concatenate[1][0]+concatenate[1][1]
prix_vol_1 = price[0][3:7]
vol_1 = [vol_1_part_1,vol_1_part_2,prix_vol_1]
print vol_1
vol_2_part_1 = concatenate[2][0]+concatenate[2][1]
vol_2_part_2 = concatenate[3][0]+concatenate[3][1]
prix_vol_2 = price[1][3:7]
vol_2 = [vol_2_part_1,vol_2_part_2,prix_vol_2]
print vol_2
vol = [(vol_1),(vol_2)]
#vol = zip(vol_1,vol_2,price)
print vol

#enregistrement
file=open("result_vol_1","w")
fichier=file.write(str(vol_1))
file.close()

#test SQL
connection = sqlite3.connect("travel.db")
cursor = connection.cursor()
#var_string = ', '.join(map(str, vol))
query = 'INSERT INTO orylax VALUES (?,?,?)'
cursor.executemany(query, vol)
connection.commit() #mauvais ordre table
