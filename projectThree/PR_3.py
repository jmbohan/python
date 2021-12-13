import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# read data
df = pd.read_csv('mushrooms.csv')


# Label encoder for training data
def label_encode_fit(data, columns):
    result = data.copy()
    encoders = {}
    for column in columns:
        encoder = preprocessing.LabelEncoder()
        result[column] = encoder.fit_transform(result[column])
        encoders[column] = encoder
    return result, encoders


# normalize data
df_label, encoders1 = label_encode_fit(df, df.columns)
plt.figure(figsize=(15, 18))
# Heatmap to visualize correlation
sns.heatmap(df_label.corr(), fmt='.2f', annot=True, cmap="hot")
# save plot
plt.savefig('shroom_heatmap.png')
plt.show()

# Drop Target column
X = df_label.drop(['bruises'], axis=1)
# Target Column for training data
y = df_label['bruises']

X_train, X_test, y_train, y_test = train_test_split(X, y)

# initialize scaler
scaler = StandardScaler()
#
# # Fit only to the training data
scaler.fit(X_train)
StandardScaler(copy=True, with_mean=True, with_std=True)

# # Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Neural Network
mlp = MLPClassifier(hidden_layer_sizes=(16, 16), max_iter=2000)
mlp.fit(X_train, y_train)
predictions = mlp.predict(X_test)
y_test_results = np.array(y_test)
# confusion matrix to a numpy array
cm = np.array(confusion_matrix(y_true=y_test, y_pred=predictions))
# numpy array to pandas Dataframe
confusion = pd.DataFrame(cm, index=['poisonous', 'not_poisonous'],
                         columns=['predicted_poisonous', 'predicted_not_poisonous'])
disp = ConfusionMatrixDisplay.from_predictions(y_test_results, predictions, )
# Print Accuracy on top on confusion matrix
disp.ax_.set_title('Accuracy Score: {}'.format(accuracy_score(y_test, predictions)))
# plt.savefig('NNconfusionMatrix.png')
# plt.show()

print('Mushroom NN predicted poisonous: \n\n', classification_report(y_test, predictions, ), '\n', confusion)

# print(len(mlp.coefs_))
# print(len(mlp.coefs_[0]))
# print(len(mlp.intercepts_[0]))

##SVM

# read data
df = pd.read_csv('mushrooms.csv')
df_label, encoders1 = label_encode_fit(df, df.columns)
# pairplot to view data
# sns.pairplot(df_label, hue='class', vars=['cap-shape', 'bruises', 'gill-size', 'odor', 'gill-color'])
plt.savefig('shroom_pairplot.png')
plt.show()
# Drop Target
X = df_label.drop(['bruises'], axis=1)
# Target for training
y = df_label['bruises']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)
# Use svc because we are using only two features
svc_model = SVC()
svc_model.fit(X_train, y_train)
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape='ovr', degree=3, gamma='auto',
    kernel='rbf', max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)
y_predict = svc_model.predict(X_test)
# confusion matrix to numpy array
cm = np.array(confusion_matrix(y_test, y_predict, labels=[1, 0]))
# numpy array to pandas Dataframe
confusion = pd.DataFrame(cm, index=['poisonous', 'not_poisonous'],
                         columns=['predicted_poisonous', 'predicted_not_poisonous'])
print('Mushroom poisonous SVM prediction: \n\n', confusion, '\n')
print(classification_report(y_test, y_predict))

fig, ax = plt.subplots(figsize=(10, 7))
# Barchart
sns.countplot(data=df, x='bruises', hue='class', palette='Purples')
# save plot
plt.savefig('shroom_bar.png')
plt.show()
