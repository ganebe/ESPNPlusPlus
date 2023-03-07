# The following reference was heavily used to create this file:
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html

import mysql.connector
from mysql.connector import errorcode
from mysql.connector.cursor import MySQLCursor

# Database and table utils

def use_database(cursor: MySQLCursor, database_name: str) -> bool:
    try:
        print(f"Using database '{database_name}': ", end='')
        cursor.execute(f"USE {database_name}")
    except mysql.connector.Error as e:
        print(e.msg)
        if(e.errno == errorcode.ER_BAD_DB_ERROR):
            if(create_database(cursor, database_name)):
                print(f"Using database '{database_name}': OK.")
                cursor._cnx.database = database_name
                return True
        return False
    else:
        print('OK')
        return True

def create_database(cursor: MySQLCursor, database_name: str) -> bool:
    try:
        print(f"Creating database '{database_name}': ", end='')
        cursor.execute(
            f"CREATE DATABASE {database_name} DEFAULT CHARACTER SET 'utf8'")
    except mysql.connector.Error as e:
        print(e.msg)
        return False
    else:
        print('OK')
        return True

def delete_database(cursor: MySQLCursor, database_name: str) -> bool:
    try:
        print(f"Deleting database '{database_name}': ", end='')
        cursor.execute(f"DROP DATABASE {database_name}")
    except mysql.connector.Error as e:
        print(e.msg)
        return False
    else:
        print('OK')
        return True

def create_table(cursor: MySQLCursor, table_name: str,
                 table_description: str) -> bool:
    try:
        database_name = cursor._cnx.database
        print(f"Creating table '{database_name}.{table_name}': ", end='')
        cursor.execute(table_description)
    except mysql.connector.Error as e:
        print(e.msg)
        return False
    else:
        print('OK')
        return True

def delete_table(cursor: MySQLCursor, table_name: str) -> bool:
    try:
        database_name = cursor._cnx.database
        print(f"Deleting table '{database_name}.{table_name}': ", end='')
        cursor.execute(f"DROP TABLE {table_name}")
    except mysql.connector.Error as e:
        print(e.msg)
        return False
    else:
        print('OK')
        return True

# Data as dictionaries utils

def insert_dict(cursor: MySQLCursor, table_name: str, data: dict) -> bool:
    try:
        columns = ', '.join(map(str, data.keys()))
        values = list(data.values())
        placeholders = ', '.join(['%s'] * len(data))
        cursor.execute(
            f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})",
            values)
    except mysql.connector.Error:
        return False
    else:
        return True

def update_dict(cursor: MySQLCursor, table_name: str, data: dict,
                key_column: str = 'id') -> bool:
    try:
        columns = map(str, data.keys())
        pairings = ', '.join(f'{column} = %s' for column in columns)
        values = list(data.values())
        cursor.execute(
            f"UPDATE {table_name} SET {pairings} WHERE {key_column} = %s",
            values + [data[key_column]])
    except mysql.connector.Error:
        return False
    else:
        return True

def delete_dict(cursor: MySQLCursor, table_name: str, data: dict,
                key_column: str = 'id') -> bool:
    try:
        cursor.execute(
            f"DELETE FROM {table_name} WHERE {key_column} = %s",
            [data[key_column]])
    except mysql.connector.Error:
        return False
    else:
        return True
