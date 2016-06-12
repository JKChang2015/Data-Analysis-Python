## 2. Sets ##

gender = []
for row in legislators:
    gender.append(row[3])
gender = set(gender)
print(gender)

## 3. Exploring the dataset ##

party = []
for row in legislators:
    party.append(row[6])
party = set(party)
print(party)
print(legislators)

## 4. Missing values ##

for row in legislators:
    if row[3] == '':
        row[3] = 'M'

## 5. Parsing birth years ##

birth_years = []
for item in legislators:
    parts = item[2].split('-')
    birth_years.append(parts[0])

## 6. Try/except blocks ##

try:
    float('hello')
except Exception:
    print("Error converting to float..")

## 7. Exception instances ##

try:
    int("")
except Exception as e:
    print(type(e))
    print(str(e))

## 8. The pass keyword ##

converted_years = []
for year in birth_years:
    try:
        year = int(year)
    except Exception:
        pass
    converted_years.append(year)

## 9. Convert birth years to integers ##

for row in legislators:
    try:
        birth_year = int(row[2].split('-')[0])
    except Exception:
        birth_year = 0
    row.append(birth_year)
    

## 10. Fill in years without a value ##

last_value = 1
for row in legislators:
    if row[7] is 0:
        row[7] = last_value
    last_value = row[7]