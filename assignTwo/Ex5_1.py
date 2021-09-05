# Ask user to enter a number  
usr_num = 0
count = 0
while True:
        str_num = input("Enter the number: ")
        if str_num == 'done':
            break
        try: 
            int_val = int(str_num)
        except:
            print('Invalid input')
            continue
        count = count + 1
        usr_num = usr_num + int_val
print("Total: " + str(usr_num) + "\nCount: " + str(count) + "\nAverage: " + str(usr_num/count)) 