from db.db_connection import db

class BaseDB:
    def __init__(self, table_name):
        self.table_name = table_name
        
    @property
    def connection(self):
        return db.connection

    def get_all(self):
        query = f'SELECT * FROM {self.table_name}'
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            return cursor.fetchall()
    
    def get_by_id(self, id:int):
        query = f'SELECT * FROM {self.table_name} WHERE id = %s'
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(query, (id,))
            return cursor.fetchone()
    
    def create(self, data:dict):
        connection = self.connection
        keys = ', '.join(data)
        holders = ''.join(['%s'] * len(data))
        query = f'''INSERT INTO {self.table_name}(
        {keys}) VALUES({holders})'''

        with connection.cursor() as cursor:
            cursor.execute(query, data.values())
            connection.commit()
            return cursor.lastrowid

    def update(self, id:int, data:dict):
        connection = self.connection
        assignments = ', '.join(f'{key} = %s' for key in data)
        query = f'''UPDATE {self.table_name} SET 
        {assignments} WHERE id = %s'''

        with connection.cursor() as cursor:
            cursor.execute(query, (*data.values(), id))
            connection.commit()
            return cursor.rowcount > 0
        
    def delete(self, id:int):
        connection = self.connection
        query = f'DELETE FROM {self.table_name} WHERE id = %s'

        with connection.cursor() as cursor:
            cursor.execute(query, (id,))
            connection.commit()
            return cursor.rowcount > 0
        