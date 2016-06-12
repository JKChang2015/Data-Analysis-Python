## 1. Regular expressions ##

strings = ["data science", "big data", "metadata"]
regex = "data"

## 2. Special characters ##

strings = ["bat", "robotics", "megabyte"]
regex = "b.t"

## 3. Beginnings and ends of string ##

strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b.tter"

## 5. Reading and printing the dataset ##

import csv
f = open("askreddit_2015.csv",'r')
post_with_header = list(csv.reader(f))
posts = post_with_header[1:len(post_with_header)]

for post in posts[0:10]:
    print(post)

## 6. Testing for matches ##

import re

of_reddit_count = 0
for post in posts:
    if re.search("of Reddit", post[0]) != None:
        of_reddit_count += 1

## 7. Accounting for inconsistencies ##

import re

of_reddit_count = 0
for row in posts:
    if re.search("of [rR]eddit", row[0]) != None:
        of_reddit_count += 1

## 8. Escaping special characters ##

import re

serious_count = 0
for row in posts:
    if re.search("\[Serious\]", row[0]) != None:
        serious_count += 1

## 9. Refining the search ##

import re

serious_count = 0
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) != None:
        serious_count += 1
        

## 10. More inconsistency ##

import re

serious_count = 0
for row in posts:
    if re.search("[\[\(][Ss]erious[\]\)]", row[0]) != None:
        serious_count += 1

## 11. Multiple regular expressions ##

import re

serious_start_count = 0
serious_end_count = 0
serious_count_final = 0

for row in posts:
    if re.search("^[\[\(][Ss]erious[\]\)]", row[0]) != None:
        serious_start_count += 1
    elif re.search("[\[\(][Ss]erious[\]\)]$", row[0]) != None:
        serious_end_count += 1
    if re.search("^[\[\(][Ss]erious[\]\)]|[\[\(][Ss]erious[\]\)]$", row[0]) != None:
        serious_count_final += 1

## 12. Substituting strings ##

import re
posts_new = []
for row in posts:
    row[0] = re.sub("[\[\(][Ss]erious[\]\)]", "[Serious]", row[0])
    posts_new.append(row)

## 13. Matching years ##

import re
print(strings)
year_strings = []
for value in strings:
    if re.search("[1-2][0-9][0-9][0-9]", value) != None:
        year_strings.append(value)
        

## 14. Repeating regular expressions ##

import re

year_strings = []
for value in strings:
    if re.search("[1-2][0-9]{3}", value) != None:
        year_strings.append(value)

## 15. Extracting years ##

import re

years = re.findall("[1-2][0-9]{3}", years_string)
        