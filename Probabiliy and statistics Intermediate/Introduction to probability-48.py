## 1. Probability basics ##

# Print the first two rows of the data.
import pandas as pd
print(flags[:2])
bars_sorted = flags.sort_values("bars",ascending=[0])
most_bars_country = bars_sorted["name"].iloc[0]
population_sorted = flags.sort_values("population",ascending=[0])
highest_population_country = population_sorted["name"].iloc[0]

## 2. Calculating probability ##

total_countries = flags.shape[0]

has_orange = len(flags[flags["orange"] == 1])
orange_probability = has_orange/total_countries

has_more_strip = len(flags[flags["stripes"] > 1])
stripe_probability = has_more_strip / total_countries

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5

ten_heads = 0.5 ** 10
hundred_heads = 0.5 ** 100

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
total_countries = flags.shape[0]
red_countries = len(flags[flags["red"] == 1])
three_red = (red_countries * (red_countries -1 ) * (red_countries -2 )) / (total_countries * (total_countries -1 ) * (total_countries -2 )) 

## 5. Disjunctive probability ##

import random

start = 1
end = 18000

nums = 18000 / 100
hundred_prob = nums / 18000
nums = int(18000/70)
seventy_prob = nums / 18000

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None

num_red = len(flags[flags["red"] == 1])
num_orange = len(flags[flags["orange"] == 1])
red_and_orange = len(flags[(flags["red"] == 1) & (flags["orange"] == 1)])
red_or_orange = (num_red + num_orange - red_and_orange)/flags.shape[0]

num_stripes = len(flags[flags["stripes"] >= 1])
num_bars = len(flags[flags["bars"] >= 1])
stripes_and_bars = len(flags[(flags["stripes"] >= 1) & (flags["bars"] >= 1)])
stripes_or_bars = (num_stripes + num_bars - stripes_and_bars)/flags.shape[0]


## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None
heads_or = 1 - (0.5) ** 3