from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

import models
import schemas
from database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Expense splitter is running"}


@app.post("/users", response_model=schemas.UserOut, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.scalar(select(models.User).where(models.User.email == user.email))
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return db.scalars(select(models.User)).all()