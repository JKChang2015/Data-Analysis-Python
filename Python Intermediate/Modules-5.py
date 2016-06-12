## 3. The math module ##

import math
a = math.sqrt(16.0)
b = math.ceil(111.3)
c = math.floor(89.9)

## 4. Variables within modules ##

import math

print(math.pi)
a = math.sqrt(math.pi)
b = math.ceil(math.pi)
c = math.floor(math.pi)

## 5. The csv module ##

import csv
nfl = list(csv.reader(open("nfl.csv",'r')))

## 6. Counting how many times a team won ##

import csv
f = open("nfl.csv")
fread = csv.reader(f)
nfl_list = list(fread)
counter = 0
for nfl_game in nfl_list:
    if nfl_game[2] == "New England Patriots":
        counter += 1
patriots_wins = counter

## 7. Making a function to count wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here
def nfl_wins(team_name):
    wins = 0
    for team in nfl:
        if team[0] in ["2009","2010","2011","2012","2013"] and team[2] == team_name:
            wins += 1
    return(wins)

cowboys_wins = nfl_wins("Dallas Cowboys")
falcons_wins = nfl_wins("Atlanta Falcons")

## 10. Working with boolean operators ##

a = 5
b = 10
# a == 5
result1 = True

# a < 5 or b > a
result2 = True

# a < 5 and b > a
result3 = False

# a == 5 or b == 5
result4 = True

# a > b or a == 10
result5 = False

## 11. Counting wins in a given year ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

def nfl_wins_in_a_year(team,year):
    count = 0
    for row in nfl:
        if row[2] == team and row[0] == year:
            count = count + 1
    return count

browns_2010_wins = nfl_wins_in_a_year("Cleveland Browns", "2010")
eagles_2011_wins = nfl_wins_in_a_year("Philadelphia Eagles", "2011")