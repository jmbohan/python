# week 2
_wage_ = 0;

while _wage_ < 7.50 or not float:
    _wage_= float(input("What is the hourly wage? "))
    if _wage_ < 7.50 or not float:
        print("wage is not valid")

else:
    _pay_ = str(_wage_ * 40)
    print("You should pay your employee " + _pay_+ " dollars")
