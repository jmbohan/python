# read and write files
'''
import random
fout = open('nums.txt', 'w') 
for x in range(10):
    myrand = random.randint(1,50)
    fout.write(str(myrand)+ "\n")
fout.close()

fin = open('nums.txt', 'r')
mylist = []
for line in fin:
    line = line.rstrip()
    mylist.append(int(line))
print(sum(mylist)/len(mylist))
'''
# read from one line 
'''
import random
fout = open('nums.txt', 'w') 
for x in range(10):
    myrand = random.randint(1,50)
    fout.write(str(myrand)+ "")
fout.close()
fin = open('nums.txt', 'r')
mylist = []
line = fin.read().split()
for i in line:
    mylist.append(int(i))
print(sum(mylist)/len(mylist))
'''
'''
# simple CSV reader 
import csv
f = open('Pilots1.csv', 'r')
reader = csv.reader(f)
for row in reader:
    print(row)
f.close() 
'''
# get a list from a csv file
'''
import csv
f = open('Pilots1.csv', 'r')
myreader = csv.reader(f)
lt = []
for row in myreader:
    lt.append(row)
print(lt)
f.close()
'''
# write the list to a new csv file 
'''
import csv
with open('mycsv.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter= ',')
    for line in lt:
        writer.writerow(line)
'''
'''
import csv

mylist = []
while True:
    name = input('Insert Fruit name: ')
    if name == 'done': break
    num = int(input('Insert Fruit number: '))
    mylist.append([name,num])
with open('names.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, csv.excel)
    writer.writerow(["fruit", "count"])
    for line in mylist:
        writer.writerow(line)
csvfile.close
'''












