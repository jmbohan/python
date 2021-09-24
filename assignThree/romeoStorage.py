import string
change = str.maketrans("","", string.punctuation)

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
     line = line.strip().lower().translate(change)
     words = line.split()
     for word in words:
         counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items():
    newtup = (key, val)
    lst.append(newtup)

lst = sorted(lst)

for key, val in lst:
    print(key) 

