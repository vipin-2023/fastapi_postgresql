from fastapi import FastAPI
import  models
from database import engine
from routers import router
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
