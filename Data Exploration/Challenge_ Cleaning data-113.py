## 4. Filter out the bad years ##

import matplotlib.pyplot as plt
%matplotlib inline
true_avengers = pd.DataFrame()

avengers['Year'].hist()
true_avengers = avengers[avengers["Year"] >= 1960]


## 5. Consolidating deaths ##

columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
true_avengers[columns]

def clean_deaths(row):
    num_deaths = 0
    columns = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
    
    for c in columns:
        death = row[c]
        if pd.isnull(death) or death == 'NO':
            continue
        elif death == 'YES':
            num_deaths += 1
    return num_deaths

true_avengers['Deaths'] = true_avengers.apply(lambda row:clean_deaths(row), axis = 1)

## 6. Years since joining ##

joined_accuracy_count  = int()
is_years_joining_55 = (true_avengers["Years since joining"] == (2015-true_avengers["Year"]))
for value in is_years_joining_55:
    if value == True:
        joined_accuracy_count += 1
        