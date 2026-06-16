from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from mysql.connector import IntegrityError
from db.db_connection import db
from logs.logger_config import logger
from routes.users import router as users_router

@asynccontextmanager
async def lifespan(app):
    logger.info('Loading up the server')
    db.init_db()
    db.init_tables()
    yield
    db.close()
    logger.info('Shutting down the server')

app = FastAPI(lifespan=lifespan)
app.include_router(users_router, prefix='/users', tags=['USERS'])

@app.middleware('HTTP')
def middleware(req:Request, next):
    logger.info(f'{req.url} - {req.method}')
    return next(req)

@app.exception_handler(HTTPException)
def http_exception_handler(req:Request, e:HTTPException):
    logger.warning(e.detail)
    return JSONResponse(e.detail, e.status_code)

@app.exception_handler(IntegrityError)
def http_exception_handler(req:Request, e:IntegrityError):
    logger.warning(e.msg)
    return JSONResponse(e.msg, 409)
