from pydantic import BaseModel
from typing import List

class Tudo(BaseModel):
    id : int
    item : str

    class Config:
        schema_extra = {
                "example" : {
                    "id": 1,
                    "item": "Example Schema!"
                    }
        }
class Tudoitem(BaseModel):
    item : str

    class Config:
        shema_extra = {
                "example" : {
                    "item" : "read the next chapter of the book"
                    }
    }
class Tudoitems(BaseModel):
    tudos : List[Tudoitem]

    class Config:
        schema_extra = {
                "example":{
                    "tudos": [
                        {
                            "item": "example schema 1!"
                        },
                        {
                            "item": "example schema 2!"
                        }
                    ]
                }
            }

