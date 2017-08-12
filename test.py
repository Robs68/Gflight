import requests

#origin = input("What is your city of origin? (Three letters):    ")
#destination = input("Where would you like to travel to? (Three letters):    ")
#date = input("What day would you like to fly there? One way flights only right now. (YYYY-MM-DD):    ")

payload = {
  "request": {
    "passengers": {
      "adultCount": "1"
    },
    "slice": [
      {
        "origin": "ORY",
        "destination": "LAX",
        "date": "2017-09-10"
      }
    ],
    "solutions": "1"
  }
}

url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyC9POMBiqyNxkigQG9rBguzKDlvZU0BcAM'
r = requests.post(url, json=payload)
formatted_response = r.json()
total = formatted_response["trips"]["tripOption"][0]["saleTotal"]
print("Total:", total)
test_response = r.json()
print(test_response)
