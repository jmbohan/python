user_input =  input("Enter a list of numbers: ")
user_list = user_input.split(" 1 2")

ds = 0
odd_list = []
even_list = []

for i in user_list:
    if i % 2 == 0 :
        even_list.append(i)
    elif i == 0 :
        continue
    else:
        odd_list.append(i)
   # ds += int(i)
print("Even : ", even_list, 'Odd List: ', odd_list)
