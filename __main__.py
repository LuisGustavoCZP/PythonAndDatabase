"""
The main module of app
"""
from postgres import Postgres
from sqlite import SQLite

from utils import get_inputs

database = Postgres()

TABLE = 'table_name'
COLUMNS = [('column1', 'varchar(255)'), ('column2', 'varchar(255)')]

database.create(TABLE, [f"{column[0]} {column[1]}" for column in COLUMNS])

data = get_inputs('Insira a', COLUMNS)
result = database.insert(TABLE, data)
print(f"Insert {result}")

result = database.select(TABLE)
print(f"Select {result}")

where = get_inputs('Selecione a', COLUMNS)
result = database.select(TABLE, where)
print(f"Select {result}")

data = get_inputs('Atualize a', COLUMNS)
where = get_inputs('Onde a', COLUMNS)
result = database.update(TABLE, data, where)
print(f"Update {result}")

""" 
where = get_inputs('Delete onde', COLUMNS)
result = database.delete(TABLE, where)
print(f"Delete {result}") 
"""
