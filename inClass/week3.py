''' using length to validate input
# ask for a six digit number and print to the console
flag = True
while flag == True:
    try:
        usr_num = input("Please enter a six digit number: ")
        if float(usr_num):
            if len(usr_num) > 6 :
                    print("Number is too big!")
            elif len(usr_num) < 6:
                    print("Number is too small!")
            else:
                print(usr_num)
                flag = False
    except:
        print("you did not enter a number")
        pass
''' 
'''Superficial string traversal 
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
fruit = 'Banana'
for letter in fruit :
    print(letter)
'''
''' counting 
word = 'banana'
count = 0 
for letter in word :
    if letter == 'a':
        count = count + 1 
print(count) 
'''
''' counting vowles in a string
my_string = input("Insert a string: ")
count = 0 
for letter in my_string:
    if letter in ['a', 'o', 'u', 'i', 'e']:
        count = count + 1 
print(count)
'''
''' Check for existence with keyword in
fruit = 'orange'
if 'g' in fruit:
    print('Might be grapefruit!')
elif 'o' in fruit:
    print('Might be an orange')
'''
