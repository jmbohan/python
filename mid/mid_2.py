#Question 2 midterm
while True:
    div = []
    try:
        n = input("Please enter a number: \n")
        if n == 'done': break
        num = int(n)
        print(type(num), num)
        for i in range(num):
            if i % n == 0:
                div.append(i)
                print(div)
    except:
        print("Enter an integer or 'done' : ")
        continue
