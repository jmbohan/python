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
fruit = 'oranged
if 'g' in fruit:
    print('Might be grapefruit!')
elif 'o' in fruit:
    print('Might be an oange')
'''
'''slice a string 
my_string = input("Insert a string: ")
for letter in range(len(my_string)):
    if my_string[letter] == '@':
        new_string = my_string[letter + 1:]
        break
'''
'''slice a string pt 2'''
my_string = input("Insert a string: ")
for letter in range(len(my_string)):
    if my_string[letter] == '@':
        break
new_string = "" 
for letter2 in range (letter + 1, len(my_string)):
    if my_string[letter2] == '@':
        new_string = my_string[letter + 1: letter2]
        break
print(new_string)