from fastapi import APIRouter
from tudo import tudo_router

app= APIRouter()

@app.get("/")
async def welcome() -> dict:
    return {
            "message" : "Hellow World"
    }
app.include_router(tudo_router)
