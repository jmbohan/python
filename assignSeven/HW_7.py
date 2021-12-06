# I have chosen to use Neural Networks and Naïve Bayes. The features I choose were ones that I felt had a
# relatively high chance of being chocolate.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import datasets
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split



candy = pd.read_csv('candy-data.csv')

X = candy.drop(['chocolate', 'competitorname', 'winpercent', 'fruity','hard', 'pricepercent'], axis=1)
y = candy['chocolate']
X_train, X_test, y_train, y_test = train_test_split(X, y)

scaler = StandardScaler()
# Fit only to the training data
scaler.fit(X_train)
StandardScaler(copy=True, with_mean=True, with_std=True)
# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=(16, 16), max_iter=2000)
mlp.fit(X_train, y_train)
predictions = mlp.predict(X_test)
y_test_results = np.array(y_test)
candy_confMatrix = confusion_matrix(y_true=y_test, y_pred=predictions)
disp = ConfusionMatrixDisplay.from_predictions(y_test_results, predictions,)
disp.ax_.set_title('Accuracy Score: {}'.format (accuracy_score(y_test, predictions)))
plt.show()

print(classification_report(y_test, predictions))

print(len(mlp.coefs_))
print(len(mlp.coefs_[0]))
print(len(mlp.intercepts_[0]))


# Naïve Bayes.

nav_candy = pd.read_csv('candy-data.csv')

X = nav_candy.drop(['chocolate', 'competitorname', 'winpercent', 'fruity','hard', 'pricepercent'], axis=1)
y = nav_candy['chocolate']
# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
gnb = GaussianNB()
mnb = MultinomialNB()
y_pred_gnb = gnb.fit(X_train, y_train).predict(X_test)
cnf_matrix_gnb = confusion_matrix(y_test, y_pred_gnb)
print('Gaussian: \n', cnf_matrix_gnb)
y_pred_mnb = mnb.fit(X_train, y_train).predict(X_test)
cnf_matrix_mnb = confusion_matrix(y_test, y_pred_mnb)
print('Multinomial: \n',cnf_matrix_mnb)
disp = ConfusionMatrixDisplay.from_predictions(y_test, y_pred_mnb, cmap='plasma')
disp.ax_.set_title('Accuracy Score: {}'.format (accuracy_score(y_test, y_pred_mnb)))
plt.show()
print(classification_report(y_test, y_pred_mnb))
