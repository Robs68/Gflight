import sqlite3
from operator import itemgetter, attrgetter
import csv


print ("exploitation des donnees")

conn = sqlite3.connect("travel.db")
cursor = conn.cursor()
cursor.execute("""SELECT prix FROM orylax""")
var2 = []
for row in cursor:
	var1 = int(float(''.join(map(str,row))))
	var2.append(var1)
var3=sorted(var2)
min=var3[0]

cursor.execute("SELECT duree FROM orylax ORDER BY prix ASC")
prix_min_duree = cursor.fetchone()	
cursor.execute("SELECT duree FROM orylax ORDER BY duree ASC")
duree_min = cursor.fetchone()
cursor.execute("SELECT heure_depart FROM orylax ORDER BY duree ASC")
heure_depart = cursor.fetchone()

date = heure_depart[0][0:10]
heure = heure_depart[0][11:16]	

def heure_UTC():
	heure_for_utc = int(heure_depart[0][11:13])
	signe = heure_depart[0][16:17]
	decalage = int(heure_depart[0][17:19])
	if signe == '+':
		h_utc = heure_for_utc+decalage
	else:
		h_utc = heure_for_utc-decalage

heure_UTC()

#vol 2D
#cursor.execute("select heure_depart,prix from orylax ORDER BY prix ASC LIMIT 10")
cursor.execute("select heure_depart,prix from orylax ORDER BY prix")
vol_2D = cursor.fetchall()

def format_date_2D():
        element=vol_2D[i][0]
        change_date=element[0:10]
	return change_date
for i in range(0,10):
	vol_2D[i]=(format_date_2D(),vol_2D[i][1])

#vol 3D
#cursor.execute("select heure_depart,prix,duree from orylax ORDER BY prix ASC LIMIT 10")
cursor.execute("select heure_depart,prix,duree from orylax ORDER BY prix")
vol_3D=cursor.fetchall()

def format_date_3D():
	element=vol_3D[i][0]
        change_date=element[0:10]
        return change_date
for i in range(0,10):
	vol_3D[i]=(format_date_3D(),vol_3D[i][1],vol_3D[i][2])

#ecriture du CSV 2D
with open('file_orylax_2D.csv','wb') as out:
	csv_out=csv.writer(out)
	for row in vol_2D:
		csv_out.writerow(row)

#ecriture du CSV 3D
with open('file_orylax_3D.csv','wb') as out:
        csv_out=csv.writer(out)
        for row in vol_3D:
                csv_out.writerow(row)

print ("fin")
