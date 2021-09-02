# ask fir a six digit number and print to the console
flag = True
while flag == True:
    try:
        usr_num = input("Please enter a six digit number: ")
        if len(usr_num) > 6 :
                print("Number is too big!")
        elif len(usr_num) < 6:
                print("Number is too small!")
        else:
            print(usr_num)
            flag = False
    except:
        pass
