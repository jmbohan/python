name = input('Enter file: ')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] =counts.get(word, 0) +1

big_count = None
big_word = None
for word, count in list(counts.items()):
    if big_count is None or count >big_count:
        big_word = words
        big_count = counts

print(big_word, big_count)
