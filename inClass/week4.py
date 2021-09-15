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
'''search a list '''
lst_one = [1,2,3,'apple',5]
lst_two = []
for str in lst_one:
    lst_two.append
print(lst_two)

















