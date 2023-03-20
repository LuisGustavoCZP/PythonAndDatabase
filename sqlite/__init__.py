"""
Provides SQLite connection
"""

from os import getenv
import dotenv
import sqlite3

dotenv.load_dotenv()

class SQLite:
    """
    SQLite Abstraction
    """
    def __init__(self) -> None:
        self.con = sqlite3.connect('./sqlite/db.sqlite')
        self.cursor = self.con.cursor()

    def create (self, table, columns:list[str]):
        """
        SQLite Create Table
        """
        columns = ", ".join(map(str, columns))
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table} ({columns});')
        self.con.commit()

    def insert (self, table, values=dict):
        """
        SQLite Insert Function
        """
        keys = tuple(values.keys())
        values = tuple(values.values())
        key_string = ", ".join(map(str, keys))
        value_string = ", ".join(map(str, ['?' for v in values]))
        query = f'INSERT INTO {table} ({key_string}) VALUES ({value_string}) RETURNING *;'

        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        self.con.commit()
        return result

    def select (self, table, where:dict=None):
        """
        SQLite Select Function
        """
        where_items = []
        values = []
        if where is not None and where != {}:
            items = list(where.items())
            where_items = [f'{item[0]} = ?' for item in items]
            values = [item[1] for item in items]

        where_string = ''
        if len(where_items) > 0:
            where_string = f" WHERE {' AND '.join(map(str, where_items))}"

        query = f'SELECT * FROM {table}{where_string};'
        #print(f'{query}\n{values}')
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def update (self, table, values, where:dict=None):
        """
        SQLite Update Function
        """
        where_items = []
        where_values = []
        if where is not None and where != {}:
            items = list(where.items())
            where_items = [f'{item[0]} = ?' for item in items]
            where_values = [item[1] for item in items]

        where_string = ''
        if len(where_items) > 0:
            where_string = f" WHERE {' AND '.join(map(str, where_items))}"

        items = list(values.items())
        set_items = [f'{item[0]} = ?' for item in items]
        set_values = [item[1] for item in items]
        set_string = f"{', '.join(map(str, set_items))}"

        query = f'UPDATE {table} SET {set_string}{where_string} RETURNING *;'

        vals = set_values+where_values
        #print(f'{query}\n{vals}')

        self.cursor.execute(query, vals)
        result = self.cursor.fetchall()
        self.con.commit()
        return result

    def delete (self, table, where:dict=None):
        """
        SQLite Delete Function
        """
        where_items = []
        values = []
        if where is not None and where != {}:
            items = list(where.items())
            where_items = [f'{item[0]} = ?' for item in items]
            values = [item[1] for item in items]

        where_string = ''
        if len(where_items) > 0:
            where_string = f" WHERE {' AND '.join(map(str, where_items))}"

        query = f'DELETE FROM {table}{where_string} RETURNING *;'
        #print(f'{query}\n{values}')

        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        self.con.commit()
        return result
