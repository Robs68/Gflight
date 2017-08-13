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


for i in test : 
#	print i['leg']
	test2 = i['leg']
	for o in test2:
		destination = o['destination']
		origine = o['origin']
		print("origine :",origine, "destination :", destination)
		#print o['destination']

trip = destination + origine

print trip
