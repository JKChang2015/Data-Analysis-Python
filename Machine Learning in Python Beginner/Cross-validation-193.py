## 2. Holdout validation ##

import numpy as np
admissions = pd.read_csv("admissions.csv")
admissions["actual_label"] = admissions["admit"]
admissions = admissions.drop("admit", axis=1)
admission_rand = np.random.permutation(admissions.index)
shuffled_admissions = admissions.loc[admission_rand]
train = shuffled_admissions.iloc[0:515]
test = shuffled_admissions.iloc[515:len(shuffled_admissions)]
shuffled_admissions.head()



## 3. Accuracy ##

from sklearn.linear_model import LogisticRegression
shuffled_index = np.random.permutation(admissions.index)
shuffled_admissions = admissions.loc[shuffled_index]
train = shuffled_admissions.iloc[0:515]
test = shuffled_admissions.iloc[515:len(shuffled_admissions)]
regressor = LogisticRegression()
regressor.fit(train[["gpa"]], train["actual_label"])
predicted_label = regressor.predict(test[["gpa"]])
test["predicted_label"] = predicted_label
true_positive_filter = (test["predicted_label"] == test["actual_label"])
true_positives = len(test[true_positive_filter])
accuracy = true_positives/len(test)
print(accuracy)



## 4. Sensitivity and specificity ##

model = LogisticRegression()
model.fit(train[["gpa"]], train["actual_label"])
labels = model.predict(test[["gpa"]])
test["predicted_label"] = labels
matches = test["predicted_label"] == test["actual_label"]
correct_predictions = test[matches]
accuracy = len(correct_predictions) / len(test)
true_positive_filter = (test["predicted_label"] == 1) & (test["actual_label"] == 1)
true_positive = len(test[true_positive_filter])
false_negative_filter = (test["predicted_label"] == 0) & (test["actual_label"] == 1)
false_negative = len(test[false_negative_filter])
sensitivity = true_positive / (false_negative + true_positive)
true_negative_filter = (test["predicted_label"] == 0 ) & (test["actual_label"] == 0)
false_positive_filter = (test["predicted_label"] == 1) & (test["actual_label"] == 0)
true_negative = len(test[true_negative_filter])
false_positive = len(test[false_positive_filter])
specificity = true_negative / (true_negative + false_positive)

print(sensitivity)
print(specificity)

## 6. ROC curve ##

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve 
from sklearn.linear_model import LogisticRegression
%matplotlib inline
regressor = LogisticRegression()
regressor.fit(train[["gpa"]], train["actual_label"])
predicted_label = regressor.predict(test[["gpa"]])
prob = regressor.predict_proba(test[["gpa"]])
fpr,tpr, thresholds = roc_curve(test["actual_label"], prob[:,1])
plt.plot(fpr,tpr)
plt.show()

## 7. Area under the curve ##

# Note the different import style!
from sklearn.metrics import roc_auc_score
auc_score = roc_auc_score(test["actual_label"],probabilities[:,1])
print(auc_score)
print(probabilities)