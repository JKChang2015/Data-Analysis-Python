## 1. Introduction to the data ##

import csv
f = open("nfl_suspensions_data.csv",'r')
nfl_suspensions = list(csv.reader(f))
nfl_suspensions = nfl_suspensions[1:len(nfl_suspensions)]

years = {}
for nfl_sus in nfl_suspensions:
    row_year = nfl_sus[5]
    if row_year in years:
        years[row_year] += 1
    else:
        years[row_year] = 1
print(years)

## 2. Unique values ##

unique_teams = set([item[1] for item in nfl_suspensions])
unique_games = set([item[2] for item in nfl_suspensions])
print(unique_teams)
print(unique_games)

## 3. Suspension class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]
    
third_suspension = Suspension(nfl_suspensions[2])

## 4. Tweaking the Suspension class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    def get_year(self):
        return(self.year)

missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()