from fastapi import APIRouter, Path
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
@tudo_router.get("/tudo/{tudo_id}")
async def get_single_tudo(tudo_id : int =  Path(..., title = "the id of the tudo to retrieve")) -> dict:
    for tudo in tudo_list:
        return {
                "tudo":tudo
        }
    return {
            "message": "tudo with supplied id doesn't exist."
    }
