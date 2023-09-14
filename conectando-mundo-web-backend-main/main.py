from fastapi import FastAPI,Depends
from schema.userschema import User
from repository import userrepository
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


@app.get("/hello/{name}")
async def hello_name(name:str):
    return {"message":f"Hello {name}"}


@app.post("/hello-post")
async def hello_name(user:User):
    return {"message":f"Hello {user.name}"}

@app.post("/user/create",response_model=User)
async def create_user(user:User, db: Session = Depends(get_db)):
    user=userrepository.create_user(db,user)
    return user

@app.get("/user/list",response_model=list[User])
async def list_users(db: Session = Depends(get_db)):
    users=userrepository.list_users(db)
    return users

@app.get("/user/find/{id}",response_model=User)
async def find_by_id(db:Session=Depends(get_db),id:int=0):
    print(id)
    user=userrepository.find_by_id(db,id)
    print(user)
    return user
