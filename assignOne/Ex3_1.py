# get user number
usr_input = input("Enter a score between 0.0 and 1.0: \n")
try:
    score = float(usr_input)
    if score <= 1.0:
        if score >= .9:
            print(str(score) + ' A')
        elif score >= .8:
            print(str(score) + ' B')
        elif score >= .7:
            print(str(score) + ' C')
        elif score >= .6:
            print(str(score) + ' D')
        elif score < .6:
            print(str(score) + ' F')
    else:
        print(str(score) + ' Bad score')

except:
    print(str(usr_input) + ' Bad score')
