from sqlalchemy.orm import Session, make_transient

from model import tareamodel
from schema import tareaschema

def create_tarea(db: Session, tarea: tareaschema.Tarea):
    db_tarea = tareamodel.Tarea(nombre=tarea.nombre,fecha=tarea.fecha,link=tarea.link, prioridad=tarea.prioridad)
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea


def ver_tareas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(tareamodel.Tarea).offset(skip).limit(limit).all()


def ver_tarea(db: Session, tarea_id: int):
    return db.query(tareamodel.Tarea).filter(tareamodel.Tarea.idtarea == tarea_id).first()

def update_tarea(db: Session, tarea_id:int, tarea: tareaschema.Tarea):
    db_tarea = db.query(tareamodel.Tarea).filter(tareamodel.Tarea.idtarea == tarea_id).first()
    if db_tarea is None:
        return None
    db_tarea.nombre = tarea.nombre or db_tarea.nombre
    db_tarea.fecha = tarea.fecha or db_tarea.fecha
    db_tarea.link = tarea.link or db_tarea.link
    db_tarea.prioridad = tarea.prioridad or db_tarea.prioridad
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

def delete_tarea(db: Session, tarea_id: int):
    db_tarea = db.query(tareamodel.Tarea).filter(tareamodel.Tarea.idtarea == tarea_id).first()
    if db_tarea is None:
        return None
    db.delete(db_tarea)
    db.commit()
    return None

def ver_prioridaduno(db: Session):
    return db.query(tareamodel.Tarea).filter(tareamodel.Tarea.prioridad == 1).all()

def ver_prioridaddos(db: Session):
    return db.query(tareamodel.Tarea).filter(tareamodel.Tarea.prioridad == 2).all()

def ver_prioridadtres(db: Session):
    return db.query(tareamodel.Tarea).filter(tareamodel.Tarea.prioridad == 3).all()