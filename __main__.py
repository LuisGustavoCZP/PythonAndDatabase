"""
The main module of app
"""
from postgres import Postgres
from sqlite import SQLite

from utils import get_inputs

database = Postgres()

TABLE = 'table_name'
COLUMNS = [('column1', 'varchar(255)'), ('column2', 'varchar(255)')]

def insertData (data = None):
    if data is None :
        result = database.insert(TABLE, data)
    else:
        result = None
    print(f"Insert {result}")

def selectData (data = None):
    if data is None :
        result = database.select(TABLE)
    else:
        result = database.select(TABLE, data)
    print(f"Select {result}")

def updateData (data = None):
    if data is None :
        result = database.update(TABLE, data)
    else:
        result = None
    print(f"Update {result}")

def deleteData (data = None):
    if data is None :
        result = database.delete(TABLE, data)
    else:
        result = None
    print(f"Delete {result}")

database.create(TABLE, [f"{column[0]} {column[1]}" for column in COLUMNS])

data = get_inputs(COLUMNS)
insertData(data)

selectData()
data = get_inputs(COLUMNS)
selectData(data)

data = get_inputs(COLUMNS)
updateData(data)
