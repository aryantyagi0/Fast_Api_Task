from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime

# Create a new user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        address=user.address,
        created_at=datetime.utcnow(),  # ✅ fixed comma
        age=user.age,
        city=user.city
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get all users
def get_users(db: Session):
    return db.query(models.User).all()

# Get a single user by ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Get a single user by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Update an existing user
def update_user(db: Session, user_id: int, user_data: schemas.UserUpdate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None

    # Only update fields provided in the request
    for field, value in user_data.model_dump(exclude_unset=True).items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user

# Delete a user
def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
