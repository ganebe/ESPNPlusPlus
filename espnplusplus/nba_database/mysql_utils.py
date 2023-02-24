# The following reference was heavily used to create this file:
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html

import mysql.connector
from mysql.connector import errorcode

import nba_schema

# DATABASE UTILS

def use_database(cursor, database_name):
    try:
        print(f'Using database "{database_name}": ', end='')
        cursor.execute(f"USE {database_name}")
    except mysql.connector.Error as e:
        print(f'Database "{database_name}" does not exist.')
        if(e.errno == errorcode.ER_BAD_DB_ERROR):
            if(create_database(cursor, database_name)):
                print(f'Using database "{database_name}": OK.')
                cursor._cnx.database = database_name
                return True
        else:
            print(e.msg)
        return False
    else:
        print('OK')
        return True

def create_database(cursor, database_name):
    try:
        print(f'Creating database "{database_name}": ', end='')
        cursor.execute(
            f"CREATE DATABASE {database_name} DEFAULT CHARACTER SET 'utf8'")
    except mysql.connector.Error as e:
        print(e.msg)
        return False
    else:
        print('OK')
        return True

def delete_database(cursor, database_name):
    try:
        print(f'Deleting database "{database_name}": ', end='')
        cursor.execute(f"DROP DATABASE {database_name}")
    except mysql.connector.Error as e:
        print(e.msg)
        return False
    else:
        print('OK')
        return True

# TABLE UTILS

def create_table(cursor, table_name, table_description):
    try:
        database_name = cursor._cnx.database
        print(f'Creating table "{database_name}.{table_name}": ', end='')
        cursor.execute(table_description)
    except mysql.connector.Error as e:
        print(e.msg)
        return False
    else:
        print('OK')
        return True

def delete_table(cursor, table_name):
    try:
        database_name = cursor._cnx.database
        print(f'Deleting table "{database_name}.{table_name}": ', end='')
        cursor.execute(f"DROP TABLE {table_name}")
    except mysql.connector.Error as e:
        print(e.msg)
        return False
    else:
        print('OK')
        return True

# DATA UTILS

def insert_data(cursor, table_name, values_dict, data_name=None):
    try:
        database_name = cursor._cnx.database
        print(
            f'Inserting \'{data_name}\' into '
            f'\'{database_name}.{table_name}\': ',
            end='')
        columns = ', '.join(map(str, values_dict.keys()))
        values = list(values_dict.values())
        placeholders = ', '.join(['%s'] * len(values))
        cursor.execute(
            f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})",
            values)
    except mysql.connector.Error as e:
        print(e.msg)
        return False
    else:
        print('OK')
        return True

def update_data(cursor, table_name, values_dict, values_id='id', data_name=None):
    try:
        database_name = cursor._cnx.database
        print(
            f'Updating \'{data_name}\' in '
            f'\'{database_name}.{table_name}\': ',
            end='')
        columns = map(str, values_dict.keys())
        pairings = ', '.join(f'{column} = %s' for column in columns)
        values = list(values_dict.values())
        condition = f'{values_id} = \'{values_dict[values_id]}\''
        cursor.execute(
            f"UPDATE {table_name} SET {pairings} WHERE {condition}",
            values)
    except mysql.connector.Error as e:
        print(e.msg)
        return False
    else:
        print('OK')
        return True

if(__name__ == '__main__'):
    cnx = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'password'
    )
    cursor = cnx.cursor()
    use_database(cursor, nba_schema.DB_NAME)
    for table_name, table_description in nba_schema.TABLES.items():
        create_table(cursor, table_name, table_description)
    lebron = {
        'id': 2544,
        'first_name': 'LeBron',
        'last_name': 'James',
        'full_name': 'LeBron James',
        'is_active': 1
    }
    insert_data(cursor, 'players', lebron, 'LeBron James')
    # cnx.close()