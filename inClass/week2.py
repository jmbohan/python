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
