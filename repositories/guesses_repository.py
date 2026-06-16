from repositories.base_repository import BaseDB

class GuessesDB(BaseDB):
    def __init__(self):
        super().__init__('guesses')

    def get_guesses_by_id(self, id:int):
        return self.get_by_id(id)
    
    def get_guesses_by_user(self, id:int):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM guesses WHERE user_id = %s', (id,))
            return cursor.fetchall()
        
    def get_guesses_by_match(self, id:int):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM guesses WHERE match_id = %s', (id,))
            return cursor.fetchall()
        
    def create_post(self, data:dict):
        return self.create(data)
    
    def delete_guess(self, id:int):
        return self.delete(id)
    
guesses_db = GuessesDB()