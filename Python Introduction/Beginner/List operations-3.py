## 2. Parsing the file ##

weather_data = []
f = open("la_weather.csv","r")
list_of_rows = f.read().split('\n')
for row in list_of_rows:
    x = row.split(',')
    weather_data.append(x)
    

## 3. Getting a single column from the data ##

# weather_data has already been read in automatically to make things easier.
weather = []
for row in weather_data:
    weather.append(row[1])
    

## 4. Counting the items in a list ##

count = 0
for data in weather:
    count += 1
print(count)

## 6. Practice slicing lists ##

slice_me = [7,6,4,5,6]
slice1 = slice_me[2:4]
slice2 = slice_me[1:2]
slice3 = slice_me[3:5]

## 7. Removing the header ##

new_weather = weather[1:366]

## 8. The in statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

## 9. Weather types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for weather in weather_types:
    weather_type_found.append(weather in new_weather)
    