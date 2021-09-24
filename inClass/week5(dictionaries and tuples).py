'''Dictionary as a count of characters'''
'''
word = 'brontosaurus'
d = dict()
for c in word:
        d[c] = d.get(c,0) + 1
print(d)
'''
'''
counts = dict()
line = input('Enter a line of text:')
words = line.split()
print('Words: ', words)
print('Counting...')

for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)
'''
'''
counts = dict()
while True:
    line = input('Enter a name of an animal and a number:')
    if line == "done":
        break
    words = line.split(',')
    counts[words[0]] = int(words[1])
print('Max:', max(counts.values()), 'Average:',sum(counts.values())/len(counts.keys()))
'''

""" import string
change = str.maketrans("","", string.punctuation)
my_str = 'Hello #() World!!!'
print(my_str.translate(change))
"""
'''
color_dict = {'red' : '#FF0000',
        'green':'#008000',
        'black':'#B00000',
        'white':'#0FFFFF'}
for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))
import operator
sorted_d = sorted(color_dict.items(), key=operator.itemgetter(1))
print(sorted_d)
'''
'''
from pprint import pprint
inventory = {
        'gold':500,
        'pouch':['flint','twine','gemstone'],
        'backpack':['xylophone','dagger','bread loaf']
}

inventory['pocket']= ['seashell','strange berry','lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']=inventory['gold'] + 50

print(inventory, "\n")
pprint(inventory)
'''
# use pformat to print to a file 
'''
from pprint import pformat

my_list = [1,2, ["Hi",3,"Hello"],4, [5.098998, "aeiou",9.234435325], "abcdefghijklmnopqrstuvwxyz", 10, 20.1234567899] 
print(my_list, "\n")
formatData = pformat(my_list)
print(formatData)
'''