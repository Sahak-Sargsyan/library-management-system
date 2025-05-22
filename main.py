from fastapi import FastAPI
from infrastructure import models
from infrastructure.database import engine
from routers import member, book
from fastapi_pagination import add_pagination

app = FastAPI()
add_pagination(app)

app.include_router(member.router)
app.include_router(book.router)