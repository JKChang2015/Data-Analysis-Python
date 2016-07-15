## 2. Register DataFrame as a table ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
census2010 = df.registerTempTable('census2010')
tables = sqlCtx.tableNames
print(tables)

## 3. Querying ##

df2 = sqlCtx.sql("Select age from census2010")
df2.show()

## 4. Filtering ##

query = 'select males, females from census2010 where age>5 and age<15'
sqlCtx.sql(query).show()

## 5. Mixing functionality ##

query = "Select males, females from census2010"
df2 = sqlCtx.sql(query)
df2.describe().show()

## 6. Multiple tables ##

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.registerTempTable('census2010')

census1980 = sqlCtx.read.json("census_1980.json")

census1990 = sqlCtx.read.json("census_1990.json")


census2000 = sqlCtx.read.json("census_2000.json")

tables = sqlCtx.tableNames()
print(tables)

## 7. Joins ##

#from pyspark.sql import SQLContext

#SqlCtx = SQLContext(sc)
query = "select c2010.total,c2000.total from census2000 as c2000, census2010 as c2010 where c2000.age = c2010.age"
df = sqlCtx.sql(query)
df.show()

## 8. SQL Functions ##

query = "select sum(c2010.total), sum(c2000.total), sum(c1990.total) from census2010 as c2010, census2000 as c2000, census1990 as c1990 where c2010.age = c2000.age and c2000.age = c1990.age"

sqlCtx.sql(query).show()