## 2. Built-in functions ##

total = sum([6,11])

## 3. Overwriting a built-in function ##

sum = sum(borrower_default_count_240)
print(sum)
test = sum(principal_outstanding_240)
print(test)

## 4. Scopes ##

def find_average(column):
    length = len(column)
    total = sum(column)
    return total / length

total = sum(borrower_default_count_240)
average = find_average(principal_outstanding_240)
print(total)

## 5. Scope isolation ##

def find_average(column):
    length = len(column)
    total = sum(column)
    return total / length

def find_length(column):
    length = len(column)
    return length

length = len(borrower_default_count_240)
average = find_average(principal_outstanding_240)
principal_length = find_length(principal_outstanding_240)
print(length)
principal_length = find_length(principal_outstanding_240)
average = find_average(principal_outstanding_240)
print(principal_length)
print(average)

## 6. Scope inheritance ##

def find_average(column):
    total = sum(column)
    # In this function, we are going to pretend that we forgot to calculate the length
    return total / length

length = 10
average = find_average(principal_outstanding_240)
print(length)

## 7. Inheritance limits ##

total = 10

def find_total(column):
    total = total + sum(column)
    return total

print(find_total(principal_outstanding_240))

## 9. Global variables ##

def func():
    global b
    b = 20
func()
print(b)

## 10. Nested contexts ##

total = 10
def find_total(l):
    return total

def find_length(l):
    length = len(l)
    return length

def find_average(l):
    total = 10
    return find_total(l) / find_length(l)

find_average(principal_outstanding_240)
total = 20
default_average = find_average(borrower_default_count_240)
print(default_average)