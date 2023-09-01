from fastapi import APIRouter

tudo_router = APIRouter()

tudo_list=[]

@tudo_router.post("/tudo")
async def add_tudo(tudo:dict) ->dict:
    tudo_list.append(tudo)
    return {
            "message": "tudo added succesfully."
    }

@tudo_router.get("/tudo")
async def retrieve_tudos() -> dict:
    return {
            "tudos": tudo_list
    }

