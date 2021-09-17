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

counts = dict()
while True:
    line = input('Enter a name of animal and a number:')
    if line == "done":
        break
    words = line.split(',')
    counts[words[0]] = words[1]
print('Counts', counts)
