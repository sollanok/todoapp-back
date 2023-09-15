from pydantic import BaseModel,validator
from datetime import datetime

@validator("fecha", pre=True)
def parse_datetime(cls, v):
    return v.strftime("%Y-%m-%d %H:%M") if isinstance(v, datetime) else v

class Tarea(BaseModel):
    nombre:str = None
    fecha:datetime = None
    link:str = None
    prioridad:int = None

