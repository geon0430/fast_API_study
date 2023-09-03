from fastapi import APIRouter, Path
from model import Tudo, Tudoitem

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
@tudo_router.put("/tudo/{tudo_id}")
async def update_tudo(tudo_data: Tudoitem, tudo_id : int = Path(..., title = "the id of the tudo to be updated/")) -> dict:
    for tudo in tudo_list:
        if tudo.id == tudo_id:
            tudo.item = tudo_data.item
            return{
                    "message": "tudo updated successfully"
            }
    return{
            "message:" "tudo with supplied id doesn't exist/"
    }
@tudo_router.delete("/tudo/{tudo_id}")
async def deltete_single_tudo(tudo_id : int) -> dict:
    for index in range(len(tudo_list)):
        tudo = tudo_list[index]
        if tudo.id == tudo_id:
            tudo_list.pop(index)
            return{
                    "message": "tudo deleted successfully"
            }
    return{
            "message:" "tudo with supplied id doesn't exist"
    }
@tudo_router.delete("/tudo")
async def delete_all_tudo() -> dict:
    tudo_list.clear()
    return{
            "message": "tudos deleted successfully."
    }
