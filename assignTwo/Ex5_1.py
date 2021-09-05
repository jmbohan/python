# Ask user to enter a number  
usr_num = 0
count = 0
while True:
    try:
        usr_num = usr_num + int(input("Please enter the number: "))
        count = count + 1
        # if not int entered 
    except ValueError as ve: 
        # check for done
        # print(ve)
        if str(ve).split(": ")[1].replace("'","") == "done": 
            break
        else:
            print("You need to enter a integer")
print("Total: " + str(usr_num) + "\nCount: " + str(count) + "\nAverage: " + str(usr_num/count)) 