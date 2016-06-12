## 3. Class syntax ##

class Car():
    def __init__(self):
        self.color = "black"
        self.make = "honda"
        self.model = "accord"

black_honda_accord = Car()

print(black_honda_accord.color)

class Team():
    def __init__(self):
        self.name = "Tampa Bay Buccaneers"

bucs = Team()
print(bucs.name)

## 4. Instance methods and __init__ ##

class Team():
    def __init__(self, name):
        self.name = name

giants = Team("New York Giants")

## 6. More instance methods ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# The nfl data is loaded into the nfl variable.
class Team():
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)
    
    # Your method goes here
    def count_total_wins(self):
        count = 0
        for team in nfl:
            if team[2] == self.name:
                count += 1
        return(count)
    
    
bucs = Team("Tampa Bay Buccaneers")
bucs.print_name()

broncos = Team("Denver Broncos")
chiefs = Team("Kansas City Chiefs")

broncos_wins = broncos.count_total_wins()
chiefs_wins = chiefs.count_total_wins()


## 7. Adding to the init function ##

import csv
class Team():
    def __init__(self, name):
        self.name = name
        self.nfl = list(csv.reader(open("nfl.csv")))

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count

jaguars = Team("Jacksonville Jaguars")
jaguars_wins = jaguars.count_total_wins()

## 8. Wins in a year ##

import csv
class Team():
    def __init__(self, name):
        self.name = name
        f = open("nfl.csv", 'r')
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count = count + 1
        return count
        
    def count_wins_in_year(self,year):
        count = 0
        for row in self.nfl:
            if row[2] == self.name and row[0] == year:
                count += 1
        return(count)
    
team = Team("San Francisco 49ers")
niners_wins_2013 = team.count_wins_in_year("2013")