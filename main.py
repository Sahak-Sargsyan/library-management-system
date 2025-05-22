from fastapi import FastAPI
from infrastructure import models
from infrastructure.database import engine
from routers import member, book

app = FastAPI()

app.include_router(member.router)
app.include_router(book.router)