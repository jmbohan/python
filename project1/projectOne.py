import csv
from pprint import pformat

f = open('Pilots1.csv', 'r')
myreader = csv.reader(f)
lt = []
for row in myreader:
    lt.append(row)
format_data = pformat(lt, )
print(format_data)
f.close()
