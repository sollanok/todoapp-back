from fastapi import FastAPI,Depends
from schema.tareaschema import Tarea
from repository import tarearepository
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

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

@app.post("/tarea/hecha",response_model=Tarea)
async def delete_tarea(tarea:Tarea, db: Session = Depends(get_db)):
    tarea=tarearepository.create_tarea(db,tarea)
    return tarea

@app.get("/tarea/vertodo",response_model=list[Tarea])
async def list_users(db: Session = Depends(get_db)):
    tareas=tarearepository.ver_tareas(db)
    return tareas

@app.get("/tarea/veruna",response_model=Tarea)
async def list_users(db: Session = Depends(get_db)):
    tareas=tarearepository.ver_tarea(db)
    return tareas

@app.post("/tarea/editar",response_model=Tarea)
async def create_tarea(tarea:Tarea, db: Session = Depends(get_db)):
    tarea=tarearepository.update_tarea(db,tarea)
    return tarea