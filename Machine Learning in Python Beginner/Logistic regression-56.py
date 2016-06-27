## 2. Introduction to the data ##

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
admissions = pd.read_csv("admissions.csv")
plt.scatter(admissions["gpa"], admissions["admit"])
plt.show()

## 5. Training a logistic regression model ##

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
linear_model = LinearRegression()
linear_model.fit(admissions[["gpa"]], admissions["admit"])

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])
print(admissions[["gpa"]].shape)
print(admissions["gpa"].shape)

## 6. Plotting probabilities ##

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])
pred_probs = logistic_model.predict_proba(admissions[["gpa"]])
plt.scatter(admissions["gpa"], pred_probs[:,1])
plt.show()

## 7. Predict labels ##

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])
fitted_labels = logistic_model.predict(admissions[["gpa"]])
print(fitted_labels[0:11])
plt.scatter(admissions["gpa"], fitted_labels)