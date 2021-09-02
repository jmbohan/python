# ask fir a six digit number and print to the console
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
        else:
            print("you did not enter a number")
    except:
        print("you did not enter a number")
        pass
