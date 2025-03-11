""" relacion de uno a muchos"""
from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine)
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship, sessionmaker

db_url = "sqlite:///database.db"

engine = create_engine(db_url) #crea motor para la base de datos

Session = sessionmaker(bind=engine) #crea la sesion para acceder a la base de datos
session = Session() #se instancia la sesion y se guarda en una variable

Base = declarative_base() # crea una clase base para los modelos de la base de datos.

class BaseModel(Base):  # esta clase sera heredada a otras clases para poder construir modelos
    __abstract__ = True # no crea una tabla para esta clase, sino que solo la use como una plantilla para otras clases.
    __allow_unmapped__ = True # permite trabajar con datos que no se guardaran en la base de datos y no lance advertencia.
    
    id = Column(Integer, primary_key=True) #todas las clases que hereden de basemodel tendran su propio id
    
"cada direccion pertenece a un solo usuario"
class Address(BaseModel):
    __tablename__ = "addresses"
    city = Column(String)
    state =Column(String)
    zip_code = Column(Integer)
    user_id: Mapped[int]= mapped_column(ForeignKey("users.id")) #llave foranea seria del modelo users y sera la propiedad id (users.id)
    user: Mapped["User"] = relationship(back_populates="addresses") #con esto podemos ver a que usuario esta ligada esta direccion
    
    def __repr__(self):
        return f"<Address(id={self.id}, city='{self.city}')>"
    
    
"un usuario puede estar relacionado a una o muchas direcciones"
class User(BaseModel):
    __tablename__ = "users"
    
    name = Column(String)
    age = Column(String)
    addresses: Mapped[list["Address"]] = relationship()
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.name}')>"
    
Base.metadata.create_all(engine) # con esto se crearan todas las tablas y se le asignara un motor de base de datos