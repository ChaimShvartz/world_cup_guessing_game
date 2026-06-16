from pydantic import BaseModel

class UserModelCreating(BaseModel):
    username: str
    email: str
    password: str

class MatchModelCreating(BaseModel):
    team_a: str
    team_b: str
    match_date: str
    stage: str

class MatchModelUpdating(BaseModel):
    score_b: int
    score_a: int

class GuessModelCreating(BaseModel):
    user_id: int
    match_id: int
    guessed_score_a: int
    guessed_score_b: int
