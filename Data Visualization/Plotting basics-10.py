## 2. The dataset ##

import pandas as pd
forest_fires = pd.read_csv("forest_fires.csv")
forest_fires.head(5)

## 4. Scatter plots ##

from matplotlib import pyplot as plt
plt.scatter(forest_fires["wind"], forest_fires["area"])
plt.show()

plt.scatter(forest_fires["temp"],forest_fires["area"])
plt.show()

## 5. Line charts ##

age = [5, 10, 15, 20, 25, 30]
height = [25, 45, 65, 75, 75, 75]
plt.plot(age,height)

## 6. Bar graphs ##

area_by_y = forest_fires.pivot_table(index="Y", values="area", aggfunc=numpy.mean)
area_by_x = forest_fires.pivot_table(index="X", values="area", aggfunc=numpy.mean)
plt.bar(area_by_y.index, area_by_y)
plt.show()
plt.bar(area_by_x.index, area_by_x)
plt.show()

## 7. Horizontal bar graphs ##

area_by_month = forest_fires.pivot_table(index="month", values="area", aggfunc=numpy.mean)
area_by_day = forest_fires.pivot_table(index="day", values="area", aggfunc=numpy.mean)
plt.barh(area_by_month, range(len(area_by_month)))
plt.show()
plt.barh(area_by_day, range(len(area_by_day)))

## 8. Chart labels ##

plt.scatter(forest_fires["wind"], forest_fires["area"])
plt.xlabel("Wind speed when fire started")
plt.ylabel("Wind speed vs fire area")
plt.show()

## 9. Plot aesthetics ##

plt.style.use("fivethirtyeight")
plt.scatter(forest_fires["rain"],forest_fires["area"])
plt.show()