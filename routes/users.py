from fastapi import APIRouter, HTTPException
from repositories.users_repository import users_db
from logs.logger_config import logger
from utils import UserModelCreating

router = APIRouter()

@router.get('')
def get_all_users():
    users = users_db.get_all_users()
    if not users:
        logger.warning("There aren't users yet")
    else:
        logger.info(f'returns {len(users)} users')
    return users

@router.get('/leaderboard')
def get_leaderboard():
    leaderboard = users_db.get_leaderboard()
    if not leaderboard:
        logger.warning("There aren't users yet")
    else:
        logger.info(f'returns leaderboard: includes {len(leaderboard)} users')
    return leaderboard

@router.get('/{id}')
def get_user_by_id(id:int):
    user = users_db.get_user_by_id(id)
    if not user:
        raise HTTPException(404, 'user not found')
    logger.info('returns the user')
    return user

@router.post('', status_code=201)
def create_user(data:UserModelCreating):
    data = data.model_dump()
    id = users_db.create(data)
    logger.info('user created successfully')
    return {'id': id}

@router.delete('/{id}')
def delete_user(id:int):
    deleted = users_db.delete_user(id)
    if not deleted:
        raise HTTPException(404, 'user not found') 
    msg = 'user deleted successfully'
    logger.info(msg)
    return {'msg': msg}