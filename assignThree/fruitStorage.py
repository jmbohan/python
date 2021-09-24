
inventory = dict() 
words = dict()
# ask user for a fruit/veggie and the count of the item
while True:
    usr_inp = input("Enter a fruit or veggie and it's count or type 'done': " )
    if usr_inp == 'done': break
    words = usr_inp.split()
    inventory = words
    print(inventory)
    # inp_food =  words[0]   
    # inp_count = int(words[1])
    for k,v in inventory.items():
        print(k,v)
       # inventory[w] = inventory.get(w,0) + 1

    # print(inventory)

# print('Produce, Count\n', w, ',', inventory[w])

