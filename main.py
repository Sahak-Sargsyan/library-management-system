from fastapi import FastAPI
from infra import models
from infra.database import engine

app = FastAPI()