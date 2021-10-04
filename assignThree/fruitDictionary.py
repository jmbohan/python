usr_inp = []
while True:
        line = input("Enter a fruit or veggie and it's count on the same line separeted by a space or type 'done': " )
        if line == 'done' : break
        usr_inp.append(tuple(line.split()))
        inventory = dict(usr_inp)
        total = 0
        for k,v in inventory.items():
             value = int(v)
             inventory[k] = inventory.get(k,value)
print('Produce, Count\n')
print(inventory)
# print("{},{}".format(inventory))