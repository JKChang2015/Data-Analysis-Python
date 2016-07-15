## 1. Spark DataFrame ##

with open('census_2010.json') as f:
    for i in range(0,4):
        print(f.readline())

## 3. Schema ##

sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.printSchema()

## 4. Pandas vs Spark DataFrames ##

df.show()

## 5. Row object ##

first_five = df.head(5)
for r in first_five:
    print(r.age)

## 6. Selecting columns ##


d = df.select('age','males','females')
d.show()

## 7. Filtering rows ##

fifty_plus = df[df["age"] > 5]
fifty_plus.show()

## 8. Comparing columns ##

d = df[df['females']<df['males']]
d.show()

## 9. Spark to Pandas ##

pandas_df = df.toPandas()
pandas_df["total"].hist()