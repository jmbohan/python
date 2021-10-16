user_input =  input("Enter a list of numbers separated by whitespace: ")
user_list = user_input.split(" ")

negative_list = []
positive_list = []

for i in user_list: 
    i = int(i)
    if (i > 0 ) :
        positive_list.append(i)
    elif i == 0 :
        continue
    else:
        negative_list.append(i)
#print("+ : ", positive_list, '-: ', negative_list)
sum_positive = sum(positive_list)
sum_negative = sum(negative_list)
#print('Sum + : ', sum_positive, 'Sum - : ', sum_negative)
print(sum_positive*sum_negative)