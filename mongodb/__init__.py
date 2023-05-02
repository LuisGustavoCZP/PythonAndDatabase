"""
Provides Postgres connection
"""

from os import getenv
import dotenv
from pymongo import MongoClient, errors as DBErrors

dotenv.load_dotenv()

class MongoDB:
    """
    Postgres Abstraction
    """
    def __init__(self) -> None:
        connection = f"mongodb://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}:{getenv('DB_PORT')+'1'}/{getenv('DB_DATABASE')}?authSource=admin"
        print(connection)
        self.client = MongoClient(connection)
        self.database = self.client[getenv('DB_DATABASE')]

    def create (self, table, columns:list[str]):
        """
        Postgres Create Table
        """
        columns = ", ".join(map(str, columns))
        return self.database[table]

    def insert (self, table, values:dict=None):
        """
        Postgres Insert Function
        """
        if values is None or values == {}:
            return None

        try:
            result = self.database[table].insert_one(values).inserted_id
            return result
        except DBErrors.PyMongoError:
            return None

    def select (self, table, where:dict=None):
        """
        Postgres Select Function
        """
        try:
            result = self.database[table].find(where)
            return [x for x in result]
        except DBErrors.PyMongoError:
            return None

    def update (self, table, values:dict=None, where:dict=None):
        """
        Postgres Update Function
        """
        if values is None or values == {}:
            return None

        try:
            result = self.database[table].update_many(where, values)
            return [x for x in result]
        except DBErrors.PyMongoError:
            return None

    def delete (self, table, where:dict=None):
        """
        Postgres Delete Function
        """
        try:
            result = self.database[table].delete_many(where)
            return [x for x in result]
        except DBErrors.PyMongoError:
            return None
