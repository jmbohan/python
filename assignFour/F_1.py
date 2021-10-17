def computegrade(grade):

    while True:
        try:
            score = float(grade)
            if score <= 1.0:
                if score >= .9:
                    print(' A')
                    break
                elif score >= .8:
                    print(' B')
                    break
                elif score >= .7:
                    print(' C')
                    break
                elif score >= .6:
                    print(' D')
                    break
                elif score < .6:
                    print(' F')
                    break
            else:
                print('Bad score')
                break
        except:
            print('Bad score')
            break
computegrade(input('Enter Score: '))