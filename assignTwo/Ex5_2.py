# Ask user to enter a number  
usr_num = 0
count = 0
largest_num = None
smallest_num = None
while True:
        str_num = input("Enter the number: ")
        if largest_num is None:
            largest_num = int(str_num) 
            smallest_num = int(str_num)
        if str_num == 'done':
            break
        try: 
            int_val = int(str_num)
        except:
            print('Invalid input')
            continue
        if int_val > largest_num:
            largest_num = int_val
        elif int_val < smallest_num:
            smallest_num = int_val
        count = count + 1
        usr_num = usr_num + int_val
print("Total: " + str(usr_num) + "\nCount: " + str(count) + "\nLargest #: " + str(largest_num) +  "\nSmallest #: " + str(smallest_num))
