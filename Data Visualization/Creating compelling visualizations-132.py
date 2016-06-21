## 2. Histogram: distplot() ##

import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

sns.distplot(births['prglngth'], kde=False)
sns.plt.show()

## 3. Seaborn styling ##

import seaborn as sns
plt.hist(births["agepreg"])

## 6. Practice: customizing distplot() ##

import seaborn as sns

sns.set_style("dark")
sns.distplot(births["birthord"])
sns.axlabel("Birth number","Frequency")
sns.plt.show()

## 7. Boxplots: boxplot() ##

births = pd.read_csv('births.csv')

sns.boxplot(births["birthord"], births["agepreg"])

sns.plt.show()

## 8. Pair plot: pairplot() ##

sns.pairplot(births[["agepreg","prglngth","birthord"]])
sns.plt.show()