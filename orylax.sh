#!/bin/bash
PATH=/opt/someApp/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cd /home/pi/Documents/Flight

exec &> orylax.log
echo "Lancement script pour ORYLAX"

DATE=$(date +%F)
echo "Date actuelle : $DATE"

#week a 1 mois
for i in 1 2 3 4 5 6 7
do
DATE=$(date +%F -d "+$i day")
python2 test.py -o CDG -d LAX -date $DATE
done

#Au mois
for i in 1 2 3 4 5 6 
do
DATE=$(date +%F -d "+$i month")
python2 test.py -o CDG -d LAX -date $DATE
done

echo "script ORYLAX fini"
