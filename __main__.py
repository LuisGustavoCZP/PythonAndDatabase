"""
The main module of app
"""
from postgres import Postgres
from sqlite import SQLite

database = Postgres()

TABLE = 'table_name'
COLUMNS = [('column1', 'varchar(255)'), ('column2', 'varchar(255)')]

database.create(TABLE, [f"{column[0]} {column[1]}" for column in COLUMNS])

VAR1 = 'alguma coisa'
VAR2 = 'coisa alguma'

result = database.insert(TABLE, {COLUMNS[0][0]:VAR1, COLUMNS[1][0]:VAR2})
print(f"Test0 {result}")

result = database.select(TABLE)
print(f"Test1 {result}")

result = database.select(TABLE, {COLUMNS[0][0]:VAR1, COLUMNS[1][0]:VAR2})
print(f"Test2 {result}")

result = database.update(TABLE, {COLUMNS[0][0]:VAR2, COLUMNS[1][0]:VAR1})
print(f"Test4 {result}") 

#result = database.delete(TABLE, {COLUMNS[0][0]:VAR2, COLUMNS[1][0]:VAR1})
#print(f"Test5 {result}")
