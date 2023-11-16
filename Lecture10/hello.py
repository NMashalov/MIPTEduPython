from typing import Union
import math

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import sqlite3

from db import (
    create_table,
    create_user,
    select_users
)

from contextlib import asynccontextmanager

storage = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    storage['connector'] = sqlite3.connect(
        'user.db',check_same_thread=False
    )
    storage['cursor'] = storage['connector'].cursor()
    create_table(storage['cursor'])
    yield
    # Release connector resources
    storage['connector'].close()
    storage.clear()
      
app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/divide_zero/")
def zero():
    return 1/0

@app.post('/create_user/')
def user_create(name:str):
    create_user(name,storage['cursor'],storage['connector'])
    return f'User {name} added'

@app.get('/select_user/')
def user_select():
    return select_users(storage['cursor'])  

@app.get("/items/{item_id}/")
def read_item(item_id: int, q: Union[str, None] = None):
    # Перевожу в upper case
    if q:
        q = ''.join([letter.capitalize() for letter in q])

    return {"item_id": item_id, "q": q}

@app.get("/sum/")
def read_item(x: int, y: int):
    # Каждая вторая буква в upper case
    return x+y

@app.get("/exp/")
def read_item(x: int):
    # Каждая вторая буква в upper case
    return math.exp(x)

@app.get("/title/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Педагогика 👩‍🏫</title>
        </head>
        <body>
            <h1>Cайт педагогики в МФТИ</h1>
            <p>Лучшая кафедра</p>
            <p>Все приходите к нам</p>
            <p>У нас лучшие занятия по Python</p>
        </body>
    </html>
    """