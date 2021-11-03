'''
import matplotlib.pyplot as plt
fruits=[]
num=[]
colors=['b','r','g','c','k']
while True:
    fruit = input("insert the name of a fruit: ")
    if fruit=="done":
        break;
    else:
        fruits.append(fruit)
    num.append(int(input("insert the number of a fruit: ")))
print(fruits)
print(num)

bars = plt.bar(fruits, num)
for i in range(len(fruits)):
    bars[i].set_color(colors[i])
plt.title("Number of Fruits")
plt.xlabel("Fruit Name")
plt.ylabel("Frequency")
plt.show()
plt.savefig('fruits.png')
'''
'''
import numpy as np
import csv

wines = np.genfromtxt("winequality-red.csv", delimiter=";", skip_header=1)
print(wines[2,3])
print(wines[0:3, 3])
fourth_wine = wines[3,:]
print(fourth_wine)
print(wines[:,11].sum())

np.set_printoptions(suppress=True)

high_quality = wines[:,11] > 7
print(high_quality)
print(wines[high_quality,:][:3,:])

high_quality_and_alcohol = (wines[:,10] > 10) & (wines[:,11] > 7) 
print(high_quality_and_alcohol)
print(wines[high_quality_and_alcohol,10:])
'''

#################################PANDAS#######################
'''
import pandas as pd
myFruit = pd.Series([10,7,12,30], index=['apple','banana','plum','watermelon'])
myFruit.name="Fruit table"
myFruit.index.name="Fruit"
print(myFruit,'\n')

print(myFruit[0],'\n')

print(myFruit[[name in ['apple','pear'] for name in myFruit.index]],'\n')

print(myFruit[myFruit>10])

print(myFruit[['banana','apple']],'\n')
'''
'''
import pandas as pd
caller = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'], 'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})

other = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})

print(caller)
print(other)

A= caller.join(other, lsuffix='_caller', rsuffix='_other')
print(A)

B =caller.set_index('key').join(other.set_index('key'))
print(B)

C=caller.join(other.set_index('key'), on='key')
print(C)
'''
'''
import pandas as pd
countries = ['Germany', 'France', 'Indonesia']
inhabitants = [82.5 * 10**6, 66.9 * 10**6, 255.5 * 10**6]
capitals = ['Berlin', 'Paris', 'Jakarta']
df1 = pd.DataFrame({'country': countries,
                                 'inhabitant': inhabitants,
                                 'capital': capitals})
print(df1,'\n')
countries = ['Germany', 'Italy', 'Spain', 'Austria']
capitals = ['Berlin', 'Rome', 'Madrid', 'Vienna']
hdis = [0.926, 0.897, 0.844, 0.893]
df2 = pd.DataFrame({'country': countries, 
                                'capital': capitals,
                                'HDI': hdis})
print(df2,'\n')
print(df1.merge(df2, on='country', how='outer'),"\n")

print(df1.join(df2,how='outer', lsuffix='_df1'),"\n")

print(pd.concat([df1, df2], sort=True),"\n")
'''
'''
import pandas as pd
df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                                              'Parrot', 'Parrot'],
                                              'Max Speed': [380., 370., 24., 26.]})
print(df,"\n")
print(df.groupby(['Animal']).mean())
'''
'''
import pandas as pd
arrays = [['Falcon', 'Falcon', 'Parrot', 'Parrot'],
              ['Captive', 'Wild', 'Captive', 'Wild']]
index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))
df = pd.DataFrame({'Max Speed': [390., 350., 30., 20.]}, index=index)
print(df,"\n") 
print(df.groupby(level=0).mean(),"\n")
print(df.groupby(level=1).mean(),"\n")
'''
import pandas as pd
df = pd.DataFrame({'month': [1, 4, 7, 10],
                             'year': [2012, 2014, 2013, 2014],
                             'sale': [55, 40, 84, 31]})
print(df,"\n")
print(df.set_index('month'),"\n")

print(df.set_index(['year', 'month']),"\n")

print(df.set_index([pd.Index([1, 2, 3, 4]), 'year']),"\n")

s = pd.Series([1, 2, 3, 4])
print(df.set_index([s, s**2]),"\n")

