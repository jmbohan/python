# I have chosen to use Neural Networks 

import pandas as pd


candy = pd.read_csv('candy-data.csv')

print(candy.keys())
print(candy['chocolate'].shape)

X = candy['data']
y = cancer['target']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit only to the training data
scaler.fit(X_train)
