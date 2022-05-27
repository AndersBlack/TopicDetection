
'''
    Used to find articles containing the specified words
'''

from unzipper import txtPathConstructorTotal, txtPathGetter, loadDict
from preprocessing import constructDict

brands = ['Acura','Alfa Romeo','Audi','BMW','Bentley',
         'Buick','Cadillac','Chevrolet','Chrysler','Dodge',
         'Fiat','Ford','GMC','Genesis','Honda','Hyundai',
         'Infiniti','Jaguar','Jeep','Kia','Land Rover',
         'Lexus','Lincoln','Lotus',
         'Mitsubishi','Nissan','Polestar','Pontiac',
         'Porsche','Ram','Rivian','Rolls-Royce','Saab',
         'Saturn','Scion','Subaru','Suzuki',
         'Tesla','Toyota','Volkswagen','Volvo']

txtPathConstructorTotal()

articlePaths = txtPathGetter()

constructDict(articlePaths, brands)

path = "fullDict.txt"

loadDict(path)
