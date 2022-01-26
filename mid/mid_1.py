#Question 1 midterm
while True:
    sum = 2
    try:
        n = input("Please enter a number: \n")
        if n == 'done': break
        num = int(n)
        for i in range(num):
            #sum  += sum ** 2
            print(sum)
            sum = sum * 2
    except:
        print("Enter an integer or 'done' : ")
        continue

# I need this
