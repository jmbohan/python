import numpy as np 
import csv


with open('Hidden_Island.csv', 'r') as f:
    data = list(csv.reader(f, delimiter=','))
removedHeader = data[1:]
headerRow = data[0:1]
print(type(removedHeader))  
finalArray = np.array(removedHeader, dtype= "U30, i4, i4")
print(finalArray)