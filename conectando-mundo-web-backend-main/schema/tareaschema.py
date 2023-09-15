from pydantic import BaseModel

class Tarea(BaseModel):
    nombre:str
    fecha:str
    link:str
    prioridad:int

