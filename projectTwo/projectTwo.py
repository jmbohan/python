from os import name
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

#open csv
df = pd.read_csv('cereal.csv')
#find negative values and replace will null
df = df.replace(-1, np.NaN)
#fill null values with mean values
for column in ['carbo','sugars','potass']:
   df[column] = df[column].fillna(df[column].mean())
#apply mean method to selected columns 
cereal_means = df.loc[:,'protein':'cups'].apply(np.mean)
cereal_std = df.loc[:,'protein':'cups'].apply(np.std)
#open to file and append to it 
f = open('cereal data.txt','a+')
f.write('Cereal means: \n')
f.write(cereal_means.to_string())
f.writelines('\n\nCereal Standard Deviation: \n ')
f.write(cereal_std.to_string())
#print to console
print('Cereal Means: \n{}' '\n\nCereal Standard Deviation: \n{}'.format(cereal_means,cereal_std))

#max a list by selected column name and return the max value and save the name of the row 
calories = list(df[df['calories'] == max(df['calories'])]['name'])[0]
protein = list(df[df['protein'] == max(df['protein'])]['name'])[0]
fat = list(df[df['fat'] == max(df['fat'])]['name'])[0]
sodium = list(df[df['sodium'] == max(df['sodium'])]['name'])[0]
fiber = list(df[df['fiber'] == max(df['fiber'])]['name'])[0]
max_cereals = str('\nCereal with the most calories: {}' '\nCereal with the most protein: {}' '\nCereal with the most fat: {}'
        '\nCereal with the most sodium: {}''\nCereal with the most fiber: {}'.format(calories,protein,fat,sodium,fiber))
print(max_cereals)
f.write('\n\nCereal Max Values: \n')
f.write(max_cereals)

#get the mfr column
manufactors = df.loc[:,'mfr']
manufactors = manufactors.reset_index().melt(id_vars='index')

#plot with kind= count 
sns.catplot(
    x='value',
    data=manufactors,
    kind='count',
)
plt.xlabel('Manufactors')
plt.ylabel('Counts')
plt.title('Cereal Totals by Manufactor')
plt.savefig('manufactors.png')
plt.show()

#plot the calories per serving with the distribution of the mean
cps = df.loc[:,'calories']
cps = cps.reset_index().melt(id_vars='index')

#plot with the distribution line 
sns.displot(
    df['calories'],
    kde=True,
    bins=10
    
)

plt.axvline
plt.xlabel('calories')
plt.ylabel('Counts')
plt.title('Calorie Distribution')
plt.savefig('calories.png')
plt.show()

#boxplot  calories per manufactor
cb = pd.DataFrame(df.loc[:,['calories','name','mfr']])
cb = cb.reset_index().melt(id_vars='index')
# sns.boxplot(cb,
# x=cb['name'],
# y=cb['calories'],
# hue=cb['mfr'])
# plt.show()
sns.set(rc={"figure.figsize":(20, 15)}) 
sns.boxplot(x=df['name'],
y=df['calories'],
hue=df['mfr'],
whis=1.5,
fliersize=10)
plt.xticks(rotation=-45)
plt.savefig('mfr calories.png')
plt.show()