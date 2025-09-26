# create_tables.py
from database import engine, Base
import models  # This ensures your models are loaded

# Create all tables
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
