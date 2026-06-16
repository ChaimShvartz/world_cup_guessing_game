from repositories.base_repository import BaseDB

class MatchesDB(BaseDB):
    def __init__(self):
        super().__init__('matches')

    def get_all_matches(self):
        return self.get_all()
    
    def get_match_by_id(self, id:int):
        return self.get_by_id(id)
    
    def post_match(self, data:dict):
        return self.create(data)
    
    def get_upcoming_matches(self):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM matches WHERE match_date > NOW()')
            return cursor.fetchall()
        
    def set_result(self, id:int, score_a:int, score_b:int):
        return self.update(id, {'score_a': score_a, "score_b": score_b})
    
matches_db = MatchesDB()