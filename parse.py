import requests
import json
from pprint import pprint

print("Lancement du script")
#print("")

file = open("out2", "r")
fichier=file.read()
with open('out2') as data_file:
	data = json.load(data_file)

#pprint(data)

#print("fichier ouvert")

test = data['trips']['tripOption'][0]['slice'][0]['segment']
#print test

print("")

#for i in data[['trips']['tripOption'][0]['slice'][0]['segment']]:
#	print i[['leg'][0]['origin']]
#airport_o = data["trips"]["tripOption"][0]["slice"][0]["segment"][0]["leg"][0]["origin"]
#for x in data["trips"]["tripOption"][0]["slice"][0]["segment"][0]["leg"]:
#	print(x['airport_o'])

origine_air = []
destination_air = []
for i in test :
	current_d = [] 
	current_o = []
	destination_air.append(current_d)
	origine_air.append(current_o)
#	print i['leg']
	test2 = i['leg']
	for o in test2:
		destination = o['destination']
		origine = o['origin']
		print("origine :",origine, "destination :", destination)
		#print o['destination']
		current_d.append(destination)
		current_o.append(origine)
trip = origine_air + destination_air
#print destination_air
#print origine_air
print ("")
#pprint(origine_air)
#pprint(destination_air)
print trip
print ("")
