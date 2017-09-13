echo "Lancement script pour ORYLAX"

DATE=$(date +%F)


python test.py -o ORY -d LAX -date 2017-10-10
python test.py -o ORY -d LAX -date 2017-10-11
python test.py -o ORY -d LAX -date 2017-10-12
python test.py -o ORY -d LAX -date 2017-10-13

echo "script ORYLAX fini"
