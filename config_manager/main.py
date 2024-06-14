# config_manager/main.py
from fastapi import FastAPI
from config_manager.api.configuration import router as config_router
from config_manager.database import database

app = FastAPI()

app.include_router(config_router, prefix="/config")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

