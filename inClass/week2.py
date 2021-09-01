'''
# week 2
_wage_ = 0;

while _wage_ < 7.50 or not float:
    _wage_= float(input("What is the hourly wage? "))
    if _wage_ < 7.50 or not float:
        print("wage is not valid")

else:
    _pay_ = str(_wage_ * 40)
    print("You should pay your employee " + _pay_+ " dollars")
'''
''' my code above was off by not handling the string error
    this is the professors code
'''
'''
while True:
    try:
        wage = input("Please insert your hourly wage: \n")
        if float(wage) < 7.5:
            print ("Not Valid \n")
            continue
        else:
            salary = float(wage) * 40
            print("You should pay your workers $", salary, "dollars")
            break
    except:
        continue
'''
'''
sum = 0
while True:
    name = input("insert your favorite animal name: ")
    if name == "done":
        break
    sum += 1
print(sum)
'''
'''
sum = 0
for num in [3,41,12,9,7]:
    sum = sum + num
print(sum)
'''

bill_sum = 0
while True:
    usr_bills = input("How much money did you spend on bills? \nPress 'e' to exit or 'd' when done\n")
    try :
        if usr_bills != 'e' or 'd':
            usr_bills = float(usr_bills)
            if float(usr_bills):
                bill_sum = bill_sum + usr_bills
            else:
                break
        else:
            break
    except:
        break
print("You spent " + str(bill_sum) + " On bills")
