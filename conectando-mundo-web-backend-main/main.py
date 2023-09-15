from fastapi import FastAPI,Depends
from schema.tareaschema import Tarea
from repository import tarearepository
from database import SessionLocal, engine
from sqlalchemy.orm import Session, make_transient
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional


app=FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
async def hello_world():
    return {"message":"Hello World"}

@app.post("/tarea/nueva",response_model=Tarea)
async def create_tarea(tarea:Tarea, db: Session = Depends(get_db)):
    tarea=tarearepository.create_tarea(db,tarea)
    return tarea

@app.get("/tarea/hecha/{tarea_id}")
async def delete_tarea(tarea_id:int, db: Session = Depends(get_db)):
    tarea=tarearepository.delete_tarea(db,tarea_id)
    return f"La tarea con id {tarea_id} ha sido eliminada"

@app.get("/tarea/vertodo",response_model=list[Tarea])
async def list_users(db: Session = Depends(get_db)):
    tareas=tarearepository.ver_tareas(db)
    return tareas

@app.get("/tarea/veruna/{tarea_id}",response_model=Tarea)
async def list_users(tarea_id:int,db: Session = Depends(get_db)):
    tareas=tarearepository.ver_tarea(db,tarea_id)
    return tareas

@app.post("/tarea/editar/{tarea_id}",response_model=Optional[Tarea])
async def create_tarea(tarea_id: int, tarea:Tarea, db: Session = Depends(get_db)):
    tarea=tarearepository.update_tarea(db,tarea_id,tarea)
    return tarea

@app.get("/tarea/verprioridaduno",response_model=list[Tarea])
async def list_users(db: Session = Depends(get_db)):
    tareas=tarearepository.ver_prioridaduno(db)
    return tareas

@app.get("/tarea/verprioridaddos",response_model=list[Tarea])
async def list_users(db: Session = Depends(get_db)):
    tareas=tarearepository.ver_prioridaddos(db)
    make_transient(tareas)
    return tareas

@app.get("/tarea/verprioridadtres",response_model=list[Tarea])
async def list_users(db: Session = Depends(get_db)):
    tareas=tarearepository.ver_prioridadtres(db)
    return tareas