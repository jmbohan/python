import numpy as np
import csv


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
print(u_ind)