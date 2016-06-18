## 1. Data structures ##

import pandas as pd
fandango = pd.read_csv("fandango_score_comparison.csv")
fandango.head(2)

## 2. Integer index ##

fandango = pd.read_csv('fandango_score_comparison.csv')
series_film = fandango["FILM"]
series_rt = fandango["RottenTomatoes"]
print(series_film[0:5])
series_rt.head(5)

## 3. Custom index ##

# Import the Series object from pandas
from pandas import Series

film_names = series_film.values
rt_scores = series_rt.values
series_custom = Series(rt_scores,index = film_names)
series_custom[['Minions (2015)','Leviathan (2014)']]

## 4. Integer index preserved ##

series_custom = Series(rt_scores , index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]
fiveten = series_custom[5:10]

## 5. Reindexing ##

original_index = series_custom.index.tolist()
sorted_by_index = series_custom.reindex(sorted(original_index))

## 6. Sorting ##

sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()

## 7. Vectorized operations ##

series_normalized = series_custom/20

## 8. Comparing and filtering ##

both_criteria = series_custom[criteria_one & criteria_two]

## 9. Alignment ##

rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean = (rt_users + rt_critics) / 2