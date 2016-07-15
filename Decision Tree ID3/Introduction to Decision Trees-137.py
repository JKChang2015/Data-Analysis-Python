## 3. Converting categorical variables ##

# Convert a single column from text categories into numbers.
for name in ["workclass","education","marital_status","occupation","relationship","race","sex","native_country","high_income"]:
    col = pandas.Categorical.from_array(income[name])
    income[name] = col.codes

## 5. Performing a split ##

# Enter your code here.
private_incomes = income[income["workclass"] == 4]
public_incomes = income[income["workclass"] != 4]

## 8. Entropy ##

import math
# We'll do the same calculation we did above, but in Python.
# Passing 2 as the second parameter to math.log will take a base 2 log.
entropy = -(2/5 * math.log(2/5, 2) + 3/5 * math.log(3/5, 2))
print(entropy)
income_entropy = -((len(income[income["high_income"] == 0]) / income.shape[0] ) * math.log((len(income[income["high_income"] == 0]) / income.shape[0] ), 2) +(len(income[income["high_income"] == 1]) / income.shape[0] ) * math.log((len(income[income["high_income"] == 1]) / income.shape[0] ), 2) )

## 9. Information gain ##

import numpy

def calc_entropy(column):
    """
    Calculate entropy given a pandas Series, list, or numpy array.
    """
    # Compute the counts of each unique value in the column.
    counts = numpy.bincount(column)
    # Divide by the total column length to get a probability.
    probabilities = counts / len(column)
    
    # Initialize the entropy to 0.
    entropy = 0
    # Loop through the probabilities, and add each one to the total entropy.
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log(prob, 2)
    
    return -entropy

# Verify our function matches our answer from earlier.
entropy = calc_entropy([1,1,0,0,1])
print(entropy)

information_gain = entropy - ((.8 * calc_entropy([1,1,0,0])) + (.2 * calc_entropy([1])))
print(information_gain)
entropy = calc_entropy(income["high_income"])
med = numpy.median(income["age"])
left = income[income["age"] <= med]["high_income"]
right = income[income["age"] > med]["high_income"]

age_information_gain = entropy - ((left.shape[0] / income.shape[0]) * calc_entropy(left) + ((right.shape[0] / income.shape[0]) * calc_entropy(right)))

## 10. Finding the best split ##

def calc_information_gain(data, split_name, target_name):
    """
    Calculate information gain given a dataset, column to split on, and target.
    """
    # Calculate original entropy.
    original_entropy = calc_entropy(data[target_name])
    
    # Find the median of the column we're splitting.
    column = data[split_name]
    median = column.median()
    
    # Make two subsets of the data based on the median.
    left_split = data[column <= median]
    right_split = data[column > median]
    
    # Loop through the splits, and calculate the subset entropy.
    to_subtract = 0
    for subset in [left_split, right_split]:
        prob = (subset.shape[0] / data.shape[0]) 
        to_subtract += prob * calc_entropy(subset[target_name])
    
    # Return information gain.
    return original_entropy - to_subtract

# Verify that our answer is the same as in the last screen.
print(calc_information_gain(income, "age", "high_income"))

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

information_gains = []
for column in columns:
    information_gains.append(calc_information_gain(income,column,"high_income"))

highest_gain = columns[information_gains.index(max(information_gains))]