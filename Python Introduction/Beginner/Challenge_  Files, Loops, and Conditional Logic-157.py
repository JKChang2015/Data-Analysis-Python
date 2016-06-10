## 3. Read the file into string ##

f = open("dq_unisex_names.csv", "r")
data = f.read()

## 4. Convert the string to a list ##

f = open('dq_unisex_names.csv', 'r')
data = f.read()
data_list = data.split("\n")
first_five = [x for x in data_list[0:5]]

## 5. Convert the list of strings to a list of lists ##

f = open('dq_unisex_names.csv', 'r')
data = f.read()
data_list = data.split('\n')
print(data_list)
string_data = []

for x in data_list:
    comma_list = x.split(",")
    string_data.append(comma_list)
print(string_data)

## 6. Convert numerical values ##

print(string_data[0:5])
numerical_data = []

for l in string_data:
    x1 = l[0]
    x2 = float(l[1])
    numerical_data.append([x1,x2])
print(numerical_data[0:5])
    
    

## 7. Filter the list ##

# The last value is ~100 people
numerical_data[len(numerical_data)-1]
thousand_or_greater = []
for data in numerical_data:
    if data[1] >=1000:
        thousand_or_greater.append(data[0])
print(thousand_or_greater[0:10])