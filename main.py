from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.db_connection import db
from logs.logger_config import logger

@asynccontextmanager
async def lifespan(app):
    logger.info('Loading up the server')
    db.init_db()
    db.init_tables()
    yield
    db.connection.close()
    logger.info('Shutting down the server')


app = FastAPI(lifespan=lifespan)