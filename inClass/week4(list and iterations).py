''' .strip returms a copy and removes the whitespace
replace() searchs for a string and then replaces it 
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane' )
print(nstr)
nstr = greet.replace('o', 'X' )
print(nstr)
'''
'''facy format operator
camels = 42 
camCount = 'I have spotted %d camels' % camels
print(camCount)

print('In %d yearts I have spotted %g %s.' % (3, 0.1, 'camels'))
'''

'''String Parsing
data = 'From jason.bohan@pfw.edu Sat Jan 5 blah blah'
at_pos = data.find('@')
print(at_pos)
space_pos = data.find(' ',at_pos)
print(space_pos)
host = data[at_pos + 1 : space_pos]
print(host)
'''
'''Lists and definite loops
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year: ', friend)
print('Done')

z = ['Joesph', 'Glen', 'Sally']
for x in z:
    print('Happy New Year: ', x)
print('Done')
'''

'''add to a list
numlist = []
while True:
    try: 
        num = input('insert a number: ')
        if num == 'stop':
            break
        else:
            numlist.append(int(num))
    except:
        pass
if len(numlist):
    print(numlist,'\nThe Sum is: ', sum(numlist),'\nThe Average is: ', sum(numlist)/len(numlist))
'''
'''search a list 
lst_one = [1,2,3,'apple',5]
lst_two = []
for index in range(len(lst_one)):
    try:
        int(lst_one[index])
    except:
        lst_two.append(lst_one[index])
print(lst_two)
'''
''' 
s = [x**2 for x in range(10)]
v = [2**i for i in range(13)]
m = [x for x in s if x % 2 == 0]
print(s, v, m)
'''
'''
noprimes = [j for i in range(2,8) for j in range(i*2,50,i)]
primes = [x for x in range(2,50) if x not in noprimes]
print(primes)
'''
'''
words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)]for w in words]
print(stuff)
'''
'''
my_list = ['blueberry', 56, 32.1, 'fish']
new_list = [i for i in my_list if isinstance(i,str)]
print(new_list)
'''



