"""
Provides Postgres connection
"""

from os import getenv
import dotenv
import psycopg2

dotenv.load_dotenv()

class Postgres:
    """
    Postgres Abstraction
    """
    def __init__(self) -> None:
        self.con = psycopg2.connect(
                    host=getenv('DB_HOST'),
                    port=getenv('DB_PORT'),
                    database=getenv('DB_DATABASE'),
                    user=getenv('DB_USER'),
                    password=getenv('DB_PASSWORD'))
        self.cursor = self.con.cursor()

    def create (self, table, columns:list[str]):
        """
        Postgres Create Table
        """
        columns = ", ".join(map(str, columns))
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {table} ({columns});')
        self.con.commit()

    def insert (self, table, values:dict=None):
        """
        Postgres Insert Function
        """
        if values is None or values == {}:
            return None

        keys = tuple(values.keys())
        values = tuple(values.values())
        key_string = ", ".join(map(str, keys))
        value_string = ", ".join(map(str, ['%s' for v in values]))
        query = f'INSERT INTO {table} ({key_string}) VALUES ({value_string}) RETURNING *;'
        try:
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            self.con.commit()
            return result
        except psycopg2.DatabaseError:
            return None

    def select (self, table, where:dict=None):
        """
        Postgres Select Function
        """
        where_items = []
        values = []
        if where is not None and where != {}:
            items = list(where.items())
            where_items = [f'{item[0]} = %s' for item in items]
            values = [item[1] for item in items]

        where_string = ''
        if len(where_items) > 0:
            where_string = f" WHERE {' AND '.join(map(str, where_items))}"

        query = f'SELECT * FROM {table}{where_string};'
        #print(f'{query}\n{values}')
        try:
            self.cursor.execute(query, values)
            return self.cursor.fetchall()
        except psycopg2.DatabaseError:
            return None

    def update (self, table, values:dict=None, where:dict=None):
        """
        Postgres Update Function
        """
        if values is None or values == {}:
            return None

        where_items = []
        where_values = []
        if where is not None and where != {}:
            items = list(where.items())
            where_items = [f'{item[0]} = %s' for item in items]
            where_values = [item[1] for item in items]

        where_string = ''
        if len(where_items) > 0:
            where_string = f" WHERE {' AND '.join(map(str, where_items))}"

        items = list(values.items())
        set_items = [f'{item[0]} = %s' for item in items]
        set_values = [item[1] for item in items]
        set_string = f"{', '.join(map(str, set_items))}"

        query = f'UPDATE {table} SET {set_string}{where_string} RETURNING *;'

        vals = set_values+where_values
        #print(f'{query}\n{vals}')
        try:
            self.cursor.execute(query, vals)
            result = self.cursor.fetchall()
            self.con.commit()
            return result
        except psycopg2.DatabaseError:
            return None

    def delete (self, table, where:dict=None):
        """
        Postgres Delete Function
        """
        where_items = []
        values = []
        if where is not None and where != {}:
            items = list(where.items())
            where_items = [f'{item[0]} = %s' for item in items]
            values = [item[1] for item in items]

        where_string = ''
        if len(where_items) > 0:
            where_string = f" WHERE {' AND '.join(map(str, where_items))}"

        query = f'DELETE FROM {table}{where_string} RETURNING *;'
        #print(f'{query}\n{values}')

        try:
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            self.con.commit()
            return result
        except psycopg2.DatabaseError:
            return None
