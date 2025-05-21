from fastapi import FastAPI
from infrastructure import models
from infrastructure.database import engine

app = FastAPI()