import mysql.connector

class MySQLHandler:
    def __init__(self, **kwargs) -> None:
        self.log = True
        if('log' in kwargs):
            self.log = kwargs['log']
            del kwargs['log']
        if('autocommit' not in kwargs):
            kwargs['autocommit'] = True
        self._cnx = mysql.connector.connect(**kwargs)
        self._cursor = self._cnx.cursor()

    def execute(self, operation: str, params: list = None, multi: bool = False, log_message: str = None, log: bool = None):
        if(log is None):
            log = self.log
        try:
            if(log):
                print(log_message + ': ', end = '')
            result = self._cursor.execute(operation, params, multi)
        except mysql.connector.Error as e:
            if(log):
                print(e.msg)
            return False
        else:
            if(log):
                print('OK')
            if(result is None):
                return True
            return result

    # DATABASE METHODS

    def use_database(self, database_name: str, log: bool = None) -> None:
        if(log is None):
            log = self.log
        log_message = None
        if(log):
            log_message = f"Using database '{database_name}'"
        operation = f'USE {database_name}'
        # Try to use the database.
        database_used = self.execute(
            operation = operation, log_message = log_message)
        # If using the database failed, try to create it.
        if(not database_used):
            database_created = self.create_database(database_name, log)
            if(database_created and log):
                print(log_message + ': OK')
                self._cnx.database = database_name
            return database_created
        return database_used

    def create_database(self, database_name: str, log: bool = None) -> bool:
        if(log is None):
            log = self.log
        log_message = None
        if(log):
            log_message = f"Creating database '{database_name}'"
        operation = (f"CREATE DATABASE {database_name} "
                     f"DEFAULT CHARACTER SET 'utf8'")
        return self.execute(operation = operation, log_message = log_message)

    def drop_database(self, database_name: str, log: bool = None) -> bool:
        if(log is None):
            log = self.log
        log_message = None
        if(log):
            log_message = f"Dropping database '{database_name}'"
        operation = f'DROP DATABASE {database_name}'
        return self.execute(operation = operation, log_message = log_message)

    # TABLE METHODS

    def create_table(self, table_name: str, table_description: str, log: bool = None) -> bool:
        if(log is None):
            log = self.log
        log_message = None
        if(log):
            table_full_name = f'{self._cnx.database}.{table_name}'
            log_message = f"Creating table '{table_full_name}'"
        return self.execute(
            operation = table_description, log_message = log_message)

    def drop_table(self, table_name: str, log: bool = None) -> bool:
        if(log is None):
            log = self.log
        log_message = None
        if(log):
            table_full_name = f'{self._cnx.database}.{table_name}'
            log_message = f"Dropping table '{table_full_name}'"
        operation = f'DROP TABLE {table_name}'
        return self.execute(operation = operation, log_message = log_message)

    # DATA METHODS

    def insert_data(self, table_name: str, data: dict, data_name: str = None, log: bool = None) -> bool:
        # Logging.
        if(log is None):
            log = self.log
        log_message = None
        if(log):
            if(data_name is None):
                if('id' in data):
                    data_name = data['id']
                else:
                    data_name = 'data'
            table_full_name = f'{self._cnx.database}.{table_name}'
            log_message = f"Inserting '{data_name}' into '{table_full_name}'"
        # Prepare to execute.
        columns = ','.join(map(str, data.keys()))
        values = list(data.values())
        placeholders = ', '.join(['%s'] * len(data))
        # Execute.
        operation = (f'INSERT INTO {table_name} '
                     f'({columns}) VALUES ({placeholders})')
        params = values
        return self.execute(
            operation = operation, params = params, log_message = log_message)

    def update_data(self, table_name: str, data: dict, key_column: str = 'id', data_name: str = None, log: bool = None) -> bool:
        # Logging.
        if(log is None):
            log = self.log
        log_message = None
        if(log):
            if(data_name is None):
                if(key_column in data):
                    data_name = data[key_column]
                elif('id' in data):
                    data_name = data['id']
                else:
                    data_name = 'data'
            table_full_name = f'{self._cnx.database}.{table_name}'
            log_message = f"Updating '{data_name}' in '{table_full_name}'"
        # Prepare to execute.
        columns = map(str, data.keys())
        pairings = ', '.join(f'{column} = %s' for column in columns)
        values = list(data.values())
        condition_value = data[key_column]
        # Execute.
        operation = (f'UPDATE {table_name} SET {pairings} '
                     f'WHERE {key_column} = %s')
        params = values + [condition_value]
        return self.execute(
            operation = operation, params = params, log_message = log_message)

    def delete_data(self, table_name: str, data: str, key_column: str = 'id', data_name: str = None, log: bool = None) -> bool:
        # Logging.
        if(log is None):
            log = self.log
        log_message = None
        if(log):
            if(data_name is None):
                data_name = data
            table_full_name = f'{self._cnx.database}.{table_name}'
            log_message = f"Deleting '{data_name}' from '{table_full_name}'"
        # Execute.
        operation = f'DELETE FROM {table_name} WHERE {key_column} = %s'
        params = [data]
        return self.execute(
            operation = operation, params = params, log_message = log_message)

    def commit(self) -> None:
        self._cnx.commit()

    def rollback(self) -> None:
        self._cnx.rollback()

    def close(self, commit: bool = True) -> None:
        if(commit):
            self.commit()
        self._cursor.close()
        self._cnx.close()

if(__name__ == '__main__'):
    import nba_schema

    handler = MySQLHandler(
        host = 'localhost',
        user = 'root',
        password = 'password'
    )

    handler.use_database(nba_schema.DB_NAME)
    for table_name, table_description in nba_schema.TABLES.items():
        handler.create_table(table_name, table_description)
    player = {
        'id': 2544,
        'first_name': 'LeBron',
        'last_name': 'James',
        'full_name': 'LeBron James',
        'is_active': 1
    }
    handler.insert_data('players', player, data_name = player['full_name'])
    player['full_name'] = 'BeLron Games'
    handler.update_data('players', player, data_name = player['full_name'])
    handler.delete_data('players', 2544, data_name = player['full_name'])
    handler.close()
