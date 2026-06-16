from repositories.base_repository import BaseDB

class UsersDB(BaseDB):
    def __init__(self):
        super().__init__('users')

    def get_all_users(self):
        return self.get_all()
    
    def get_user_by_id(self, id):
        return self.get_by_id(id)
    
    def create_user(self, data:dict):
        return self.create(data)
    
    def delete_user(self, id:int):
        return self.delete(id)
    
    def get_leaderboard(self):
        query = 'SELECT username, points FROM users ORDER BY points DESC'
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            return cursor.fetchall()
        
    def increment_points_by_guess(self, id:int, points:int):
        return self.update({'points': f'points = points + %s'}, (points, id))

users_db = UsersDB()