from fastapi import FastAPI
from models.database import database

from routers import users, posts, common

app = FastAPI()

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(common.router)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()