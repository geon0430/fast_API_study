from pydantic import BaseModel

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

