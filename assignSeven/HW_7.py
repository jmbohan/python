# I have chosen to use Neural Networks
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

candy = pd.read_csv('candy-data.csv')

X = candy.drop(['chocolate', 'competitorname'], axis=1)
y = candy['chocolate']
X_train, X_test, y_train, y_test = train_test_split(X, y)

scaler = StandardScaler()
# Fit only to the training data
scaler.fit(X_train)
StandardScaler(copy=True, with_mean=True, with_std=True)
# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=10, max_iter=2000)
mlp.fit(X_train, y_train)
predictions = mlp.predict(X_test)
y_test_results = np.array(y_test)
# candy_confMatrix = confusion_matrix(y_true=y_test, y_pred=predictions)

ConfusionMatrixDisplay.from_predictions(y_test_results, predictions)
plt.show()

print(classification_report(y_test, predictions))

print(len(mlp.coefs_))
print(len(mlp.coefs_[0]))
print(len(mlp.intercepts_[0]))



# X = candy['data']
# y = cancer['target']

# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y)

# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# # Fit only to the training data
# scaler.fit(X_train)
