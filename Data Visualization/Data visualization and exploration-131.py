## 3. Customizing histograms ##

import matplotlib.pyplot as plt

columns = ['Median','Sample_size']

# Set the `layout` parameter as `(2,1)` so the graphs are displayed as 2 rows & 1 column 
# Then set `grid` parameter to `False`.
recent_grads.hist(column=columns, layout=(2,1), grid=False)

## 4. Practice: histograms ##

plt.hist(recent_grads["Sample_size"], bins = 50)

## 7. Practice: box plots ##

recent_grads[['Sample_size', 'Major_category']].boxplot(by='Major_category')
plt.xticks(rotation=90)

total = recent_grads[["Total","Major_category"]]
total.boxplot(by="Major_category")
plt.xticks(rotation=90)

## 9. Practice: multiple plots in one chart ##

plt.scatter(recent_grads["Unemployment_rate"], recent_grads["P25th"], color = 'red')
plt.scatter(recent_grads["ShareWomen"], recent_grads["P25th"], color = 'blue')
plt.show()