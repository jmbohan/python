import math as m
def func(x):
    #x = ((1/3)*(x**3))-((1/2)*(x**2))-(12*x)+3
    #x = (x**4)-(32*(x**2))-5
    #x = ((5-x)/(7+x))
    x = ((x**2)-9)**(1/9)

    return x

print('-4:', func(-4))
print('-3:', func(-3))
print('0:', func(0))
print('3:', func(3))