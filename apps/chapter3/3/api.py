from fastapi import FastAPI
from tudo import tudo_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
            "message" : "Hellow World"
    }
app.include_router(tudo_router)
