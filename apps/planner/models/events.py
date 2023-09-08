from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id : int
    title : str
    image : str
    descroption : str
    tags : List[str]
    location : str

