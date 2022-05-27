import json
from unzipper import txtPathConstructorTotal, txtPathGetter, loadDict

# brands = ['Acura','Alfa Romeo','Audi','BMW','Bentley',
#          'Buick','Cadillac','Chevrolet','Chrysler','Dodge',
#          'Fiat','Ford','GMC','Genesis','Honda','Hyundai',
#          'Infiniti','Jaguar','Jeep','Kia','Land Rover',
#          'Lexus','Lincoln','Lotus',
#          'Mitsubishi','Nissan','Polestar','Pontiac',
#          'Porsche','Ram','Rivian','Rolls-Royce','Saab',
#          'Scion','Subaru','Suzuki',
#          'Tesla','Toyota','Volkswagen','Volvo']
#
# politics = ['Biden','Trump','Senator','Politics',
#             'Johnson','Macron','Snowden','Clinton','Sanders']
#
# techs = ['Apple','Microsoft','Android','computer',
#          'smartphone','spacex','bitcoin','data',
#          'intel','amd','nvidia','hacker']
#
# sports = ['sports','football','superbowl','basketball',
#           'baseball','fifa','Ronaldo',
#           'quaterback','lebron']
#
# covids = ['covid','virus','corona','quarantine','vaccine',
#          'pfizer','astrazeneca','moderna','lockdown','infected',
#          'facemask']


brands = ['Acura','Alfa Romeo','Audi','BMW','Bentley',
         'Buick','Cadillac','Chevrolet','Chrysler',
         'Fiat','GMC','Honda','Hyundai',
         'Jeep','Kia','Land Rover',
         'Lexus',
         'Mitsubishi','Nissan','Polestar','Pontiac',
         'Porsche','Rivian','Rolls-Royce','Saab',
         'Scion','Subaru','Suzuki',
         'Tesla','Toyota','Volkswagen','Volvo']

politics = ['Biden','Trump','Brexit','Macron',
            'Snowden','Clinton','Sanders']

techs = ['Apple','Microsoft','Android','computer',
         'smartphone','spacex','bitcoin',
         'intel','amd','nvidia','hacker']

sports = ['football','superbowl','basketball',
          'baseball','fifa','Ronaldo',
          'quaterback','lebron']

covids = ['covid','virus','corona','quarantine','vaccine',
         'pfizer','astrazeneca','moderna','lockdown','infected',
         'facemask']

path = "fullDict.json"

badData = loadDict(path)

carObj = []
politObj = []
techObj = []
sportObj = []
covidObj = []

for jsonData in badData:
    for brand in brands:
        if " " + brand.lower() + " " in jsonData["tokens"]:
            carObj.append(jsonData)
            continue

    for polit in politics:
        if " " + polit.lower() + " " in jsonData["tokens"]:
            politObj.append(jsonData)
            continue

    for tech in techs:
        if " " + tech.lower() + " " in jsonData["tokens"]:
            techObj.append(jsonData)
            continue

    for sport in sports:
        if " " + sport.lower() + " " in jsonData["tokens"]:
            sportObj.append(jsonData)
            continue

    for covid in covids:
        if " " + covid.lower() + " " in jsonData["tokens"]:
            covidObj.append(jsonData)
            continue

# ---------------------- Write to files! --------------------------------

with open('carDict2.json', 'a', encoding='utf8') as data:
    json.dump(carObj, data, indent=4)

with open('politicalDict2.json', 'a', encoding='utf8') as data:
    json.dump(politObj, data, indent=4)

with open('techDict2.json', 'a', encoding='utf8') as data:
    json.dump(techObj, data, indent=4)

with open('sportsDict2.json', 'a', encoding='utf8') as data:
    json.dump(sportObj, data, indent=4)

with open('covidDict2.json', 'a', encoding='utf8') as data:
    json.dump(covidObj, data, indent=4)
