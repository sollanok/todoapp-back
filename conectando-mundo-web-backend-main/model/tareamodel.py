from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base


class Tarea(Base):
    __tablename__ = "tarea"

    idtarea = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    fecha=Column(String)
    link=Column(String)
    prioridad = Column(Integer)