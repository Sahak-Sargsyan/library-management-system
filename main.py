from fastapi import FastAPI
from infrastructure import models
from infrastructure.database import engine
from routers import member

app = FastAPI()

app.include_router(member.router)