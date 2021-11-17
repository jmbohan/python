import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

grades = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    0: "F",
}


def grade_mapping(value):
    for key, letter in grades.items():
        if value >= key:
            return letter


df = pd.read_csv('Projects.csv')
empty_frame = np.where(pd.isnull(df))
empty_frame = [df.iloc[i, j] for i, j in zip(*np.where(pd.isnull(df)))]
# drops rows that have a null value
# dropped_nan = df.dropna(axis='index', how='any')
dropped_nan = df.fillna(0)
print('\nProject one mean: {}'.format(np.mean(dropped_nan['project_one'])))
print('Project one Standard Deviation: {}'.format(np.std(dropped_nan['project_one'])))

print('\nProject two mean: {}'.format(np.mean(dropped_nan['project_two'])))
print('Project two Standard Deviation: {}'.format(np.std(dropped_nan['project_two'])))

print('\nProject three mean: {}'.format(np.mean(dropped_nan['project_three'])))
print('Project three Standard Deviation: {}'.format(np.std(dropped_nan['project_three'])))
letter_grades_one = dropped_nan['project_one'].map(grade_mapping)
letter_grades_two = dropped_nan['project_two'].map(grade_mapping)
letter_grades_three = dropped_nan['project_three'].map(grade_mapping)
dropped_nan['letter_grade_one'] = pd.Categorical(letter_grades_one, categories=grades.values(), )
dropped_nan['letter_grade_two'] = pd.Categorical(letter_grades_two, categories=grades.values(), )
dropped_nan['letter_grade_three'] = pd.Categorical(letter_grades_three, categories=grades.values(), )
# one_letter = dropped_nan.pop('letter_grade')

df = pd.DataFrame(dropped_nan,
                  columns=['first_name', 'last_name', 'age', 'project_one', 'letter_grade_one', 'project_two',
                           'letter_grade_two', 'project_three', 'letter_grade_three'])
df.to_csv('LetterGrades.csv')

project_grades = df.loc[:, ['letter_grade_one', 'letter_grade_two', 'letter_grade_three']]
first_test = pd.Series(project_grades['letter_grade_one'])
second_test = pd.Series(project_grades['letter_grade_two'])
third_test = pd.Series(project_grades['letter_grade_three'])
df = pd.concat([first_test, second_test, third_test], axis=1)
# rename
df = project_grades.reset_index().melt(id_vars=['index'])

sns.catplot(
    x='value',
    hue='variable',
    data=df,
    kind='count',
    order=['A', 'B', 'C', 'D', 'F'],
    palette=['blue', 'red', 'green'],
    legend=False
)
plt.xlabel('Grades')
plt.ylabel('Counts')
plt.title('Test Grades')
plt.legend(['Test One', 'Test Two', 'Test Three'])
plt.show()

age_plot = pd.DataFrame(dropped_nan, columns=['age', 'project_one', 'project_two', 'project_three'])
# age_plot = age_plot.reset_index().melt(id_vars=['age'])
# age_plot = age_plot.groupby(['age'])
# age_plot = age_plot.unstack()
age_plot = age_plot.set_index(['age'])
age_plot = age_plot.sort_values(by=['age'])
# age_plot = age_plot.pivot_table(index=['age'])
# age_plot = age_plot
age_plot = age_plot.reset_index().melt(id_vars='age')
sns.scatterplot(
    data=age_plot,
    y='value',
    x='age',
    hue='variable',
    legend=True
)
plt.show()
print(age_plot)