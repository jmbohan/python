# reverse a string
'''
def string_rev(str1):
    rstr1=''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index = index -1
    return rstr1

print(string_rev('1234abcd'))
'''
'''
# reverse with a for loop
def string_rev(s):
    str = ''
    for i in s:
        str = i + str
    return str

print(string_rev('1234abcd'))
'''
#recursive

'''
def string_rev(s):
    if len(s) == 0:
        return s
    else:
        return string_rev(s[1:])+ s[0]
print(string_rev('1234abcd'))
'''
# using slice
'''
def string_rev(s):
    string = s[::-1]
    return string
print(string_rev('1234abcd'))
'''
'''
def string_rev(s):
    return s[::-1]
print(string_rev('1234abcd'))
'''
# factorial
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))
'''
# append to a list
'''
def unique_list(mylist):
    unique = []
    for a in mylist:
        if a not in unique:
            unique.append(a)
    return unique

print(unique_list([1,2,3,3,3,3,4,5]))
'''
# append to a list with idiom
'''
def unique_list(mylist):
    unique=[]
    unique=[mylist[i] for i in range(len(mylist)) if mylist[i] not in mylist[i+1: ]]
    return unique

print(unique_list([1,2,3,3,3,3,4,5]))
'''
'''
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

for i in range(1,10000):
    if perfect_number(i):
        print(i)
'''
# PErfect number

'''
def perfect_number(n):
    sum = 0
    for x in range(1, n//2+1):
        if n % x == 0:
            sum += x
    return sum == n
for i in range(1,10000):
    if perfect_number(i):
        print(i)
'''
# get filename and open file 
def readfile(filename):
    fin = open(filename,'r')
    mylist = []
    for line in fin:
        line = line.split()
        for i in line:
            try:
                mylist.append(int(i))
            except:
                pass
    d = dict()
    for i in mylist:
        d[i] = d.get(i,0) + 1
    return d

filename=input("Insert the name of the file: ")
d = readfile(filename)
print(d)

