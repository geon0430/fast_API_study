from fastapi import APIRouter
from model import Tudo

tudo_router = APIRouter()

tudo_list=[]

@tudo_router.post("/tudo")
async def add_tudo(tudo: Tudo) ->dict:
    tudo_list.append(tudo)
    return {
            "message" : "todo added sucessfully."
    }

@tudo_router.get("/tudo")
async def retrieve_tudos() -> dict:
    return {
            "tudos": tudo_list
    }

