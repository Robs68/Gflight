import requests
import json
from pprint import pprint

print("Lancement du script")

file = open("out2", "r")
fichier=file.read()
with open('out2') as data_file:
	data = json.load(data_file)


test = data['trips']['tripOption'][0]['slice'][0]['segment']

#mutlievols
multivol = data['trips']['tripOption']
origine_air = []
destination_air = []
vol_entier = []
for p in multivol : 
	print("")
	multivol1 = p['slice']
	prix = p['saleTotal']
	for q in multivol1 : 
		multivol2 = q['segment']
		duree_trip = q['duration']
		duree_trip_h = duree_trip // 60
		for s in multivol2 :
			multivol3 = s['leg']
			for d in multivol3 : 
				ori = d['origin']
				dest = d['destination']
				heure_ar = d['arrivalTime']
				heure_de = d['departureTime']
				vol_entier = ori + dest
#				print vol_entier
				origine_air.append(ori)
#				print origine_air
										
print ("resultat list", origine_air)
#print destination_air
titi = []
for i in range(0,len(origine_air)):
	origine = origine_air[i][0:3] #trouve les 3 premier caracteres
	destination = origine_air[i][3:6]
	titi.append(origine)
	titi.append(destination)
print("")
print titi[0]
print titi[1]

