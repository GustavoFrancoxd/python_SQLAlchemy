from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = relationship("Address", back_populates="user", uselist=False) #relacion con direccion; uselist=False indica relacion 1 a 1
    
class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('users.id')) #llave foranea de usuario
    user = relationship("User", back_populates="address") #relacion con usuario
    
Base.metadata.create_all(engine)


new_user = User(name='John Doe')
new_address = Address(email='john@example.com', user=new_user)
session.add(new_user)
session.add(new_address)
session.commit()

"""
print(f"{new_user.name = }")
print(f"{new_address.email = }")
print(f"{new_user.address.email = }")
print(f"{new_address.user.name = }")
"""

user = session.query(User).filter_by(name='John Doe').first() #ejecutando una query
print(f"User: {user.name}, Address: {user.address.email}")