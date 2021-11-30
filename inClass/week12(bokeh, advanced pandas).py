'''
from bokeh.plotting import figure 
from bokeh.io import output_file, show
from numpy import cos, linspace

output_file("testBokeh.html", title='Bokeh Plot') 
#Display plots in html
#Use numpy to make some data
x = linspace(-6,6,100)
y  =  cos(x)

# Use Bokeh to make  a plot p
p = figure(width=500, height=500)
p.circle(x, y, size=7, color="firebrick", alpha=0.5)
show(p)
# alpha is saturation
'''
'''
from numpy import promote_types
import pandas as pd

df = pd.read_csv('Salaries.csv')
df_drop = df.loc[10:15, ['rank','sex','salary']]

df_sort = df_drop.sort_values(by=['rank','salary'], ascending=[True,False])

print(df_sort)
'''
'''
import pandas as pd
titanicDF = pd.read_csv('titanic2.csv')
print(titanicDF['Fare'].describe())
'''
import seaborn as sns
import numpy as np
import pandas as pd

def is_old_func(row):
    return row['age'] >60

titanic =sns.load_dataset('titanic')

titanFilter = titanic[(titanic.sex == 'female')
                    & (titanic['class'].isin(['First','Third'])) 
                    & (titanic.age > 30)
                    & (titanic.survived == 0)]
#print(titanFilter)

bins = [0, 12, 17, 60, np.inf]
labels = ['child', 'teenager', 'adult', 'elder']
age_groups = pd.cut(titanic.age, bins, labels=labels)
titanic['age_group'] = age_groups
groups = titanic.groupby(['age_group', 'alone'])
# print(groups.size())

titanic['is_old'] = titanic.apply(is_old_func, axis='columns')
old = titanic['is_old'] == True

print(old)