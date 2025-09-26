# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from models import Base, User  # SQLAlchemy models
import schemas, crud
from database import SessionLocal, engine

# 1️⃣ Create database tables (safe for first run)
Base.metadata.create_all(bind=engine)

# 2️⃣ Initialize FastAPI
app = FastAPI(title="User API")

# 3️⃣ Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 4️⃣ Root endpoint
@app.get("/")
def read_root():
    return {"message": "API is running!"}

# 5️⃣ Create a new user
@app.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

# 6️⃣ Read all users
@app.get("/users", response_model=List[schemas.UserOut])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# 7️⃣ Read single user by ID
@app.get("/users/{user_id}", response_model=schemas.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# 8️⃣ Update user by ID
@app.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return crud.update_user(db, db_user, user_update)

# 9️⃣ Delete user by ID
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}
