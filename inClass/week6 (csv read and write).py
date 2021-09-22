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
# another way to get a list from a csv file