
"<dialect>+<driver>://<username>:<password>@<host>:<port>/<database>"

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# Database URL for SQLite
db_url = "sqlite:///database.db"

# Create the engine
engine = create_engine(db_url)

# Base class for declarative class definitions
Base = declarative_base()

# Define the User class
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create all tables in the database
Base.metadata.create_all(engine)