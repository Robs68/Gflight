import sqlite3
from operator import itemgetter, attrgetter
import csv
import ftplib

print ("exploitation des donnees")

conn = sqlite3.connect("travel.db")
cursor = conn.cursor()

#liste BDD
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
liste_table=cursor.fetchall()
length_tuple = len(liste_table)

def supp_doublons(base_de_donnee):
	cursor.execute("delete from "+base_courante+ " where rowid not in (select min(rowid) from "+base_courante+"  group by heure_depart,prix)")
	conn.commit()
	print ("Les doublons de la base : "+base_courante+" ont ete supprimees")
	return base_courante

def format_donnee(base_de_donnee):
	cursor.execute("SELECT duree FROM "+base_courante+ " ORDER BY prix ASC")
	prix_min_duree = cursor.fetchone()
	cursor.execute("SELECT duree FROM "+base_courante+ " ORDER BY duree ASC")
	duree_min = cursor.fetchone()
	cursor.execute("SELECT heure_depart FROM "+base_courante+ " ORDER BY duree ASC")
	heure_depart = cursor.fetchone()

def heure_UTC():
	heure_for_utc = int(heure_depart[0][11:13])
	signe = heure_depart[0][16:17]
	decalage = int(heure_depart[0][17:19])
	if signe == '+':
		h_utc = heure_for_utc+decalage
	else:
		h_utc = heure_for_utc-decalage

def format_date(vol):
	change_date=vol[i][0][0:10]
	return change_date

def fichier_CSV(base_de_donnee):
	cursor.execute("select heure_depart,prix from "+base_courante+ " ORDER BY prix")
	vol_2D = cursor.fetchall()
	taille = len(vol_2D)
	for i in range(0,taille):
	        vol_2D[i]=(format_date(vol_2D),vol_2D[i][1])
	file_2D='file_2D_'+base_courante+'.csv'
	with open(file_2D,'a') as out:
        	csv_out=csv.writer(out)
	        for row in vol_2D:
        	        csv_out.writerow(row)
	cursor.execute("select heure_depart,prix,duree from "+base_courante+" ORDER BY prix")
	vol_3D=cursor.fetchall()
	for i in range(0,taille):
        	vol_3D[i]=(format_date(vol_3D),vol_3D[i][1],vol_3D[i][2])
	file_3D='file_3D_'+base_courante+'.csv'
	with open(file_3D,'a') as out:
        	csv_out=csv.writer(out)
	        for row in vol_3D:
        	        csv_out.writerow(row)
	return fichier_CSV

#main 
for i in range(length_tuple):
        base_courante=''.join(liste_table[i])
        supp_doublons(base_courante)
	fichier_CSV(base_courante)

#heure_UTC()


#Envoie fichiers vers Syno
connect = ftplib.FTP('192.168.1.17','Rasp','Tata2525!')
fichier = 'file_orylax_2D.csv'
file = open(fichier, 'rb')
connect.cwd('/home/GFlights')
connect.storbinary("STOR " + fichier,file)
file.close()
connect.quit

print ("fin")
