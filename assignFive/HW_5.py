import numpy as np
import csv

def animal_count(animal_name):
    print(animal_name)
    animal_count = 0
    for element in finalArray['Animal'] == animal_name:
        if element == True:
            animal_count = animal_count +1
    return animal_count

def convert_to_tuples(list_data):
    convert_list = []
    for row in list_data:
        new_tuple = tuple(row)
        convert_list.append(new_tuple)
    return convert_list


with open('Hidden_Island.csv', 'r') as f:
    data = list(csv.reader(f, delimiter=','))
removedHeader = data[1:]
headerRow = data[0:1]
type_spec = np.dtype([(headerRow[0][0], "U30"), (headerRow[0][1], "i4"), (headerRow[0][2], "i4")])
listConvert = convert_to_tuples(removedHeader)
finalArray = np.array(listConvert, type_spec)
animal = finalArray['Animal']
range_number = finalArray['Range']
u_ind = finalArray['Unique Individuals']
puffin_count = 0 
finalArray = finalArray.reshape(600,1)

puffin_count = animal_count('Purple Puffin')
wombat_count = animal_count('Wisteria Wombat')
pomeranian_count = animal_count('Pumpkin Pomeranian')
bichon_count = animal_count('Burgundy Bichon Frise')
print(puffin_count)
print(wombat_count)
print(pomeranian_count)
print(bichon_count)