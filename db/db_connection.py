import mysql.connector
from logs.logger_config import logger

class DB:
    def __init__(self):
        self.connect()

    def connect(self):
        self._connection = mysql.connector.connect(host='localhost', 
                                                   user='root', password='root', database='world_cup_db')
    
    @property
    def connection(self):
        if not self._connection.is_connected():
            logger.warning('Connection is lost, creating new one')
            self.connect()
        return self._connection
    
    def init_db(self):
        logger.info('Initializing the database')
        with self.connection.cursor() as cursor:
            cursor.execute('CREATE DATABASE IF NOT EXISTS world_cup_db')
            cursor.execute('USE world_cup_db')
    
    def init_tables(self):
        logger.info('Initializing the tables')
        self.init_users_table()
        self.init_matches_table()
        self.init_guesses_table()

    def init_users_table(self):
        with self.connection.cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                           id INT PRIMARY KEY AUTO_INCREMENT,
                           username VARCHAR(50) UNIQUE NOT NULL,
                           email VARCHAR(100) UNIQUE NOT NULL,
                           password VARCHAR(100) NOT NULL,
                           points INT DEFAULT 0,
                           join_date DATE DEFAULT (CURRENT_DATE)
                           )''')
            
    def init_matches_table(self):
        with self.connection.cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS matches(
                           id INT PRIMARY KEY AUTO_INCREMENT,
                           team_a VARCHAR(50) NOT NULL,
                           team_b VARCHAR(50) NOT NULL,
                           score_a INT DEFAULT NULL,
                           score_b INT DEFAULT NULL,
                           match_date DATETIME NOT NULL,
                           stage VARCHAR(30) NOT NULL
                           )''')
            
    def init_guesses_table(self):
        with self.connection.cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS guesses(
                           id INT PRIMARY KEY AUTO_INCREMENT,
                           user_id INT,
                           match_id INT,
                           guessed_score_a INT NOT NULL,
                           guessed_score_b INT NOT NULL,
                           points_earned INT DEFAULT 0
                           )''')
            
    def close(self):
        self._connection.close()
        logger.info('Closing the connection')

db = DB()
