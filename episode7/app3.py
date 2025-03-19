from sqlalchemy import ForeignKey, create_engine, select, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, sessionmaker, relationship
from typing import Optional
from utils import str_100, str_20

# URL de la base de datos
db_url = 'sqlite:///database.db'

# Crear el motor de la base de datos
engine = create_engine(db_url, echo=True)

# Crear la clase base
class Base(DeclarativeBase):
    pass

# Definir el modelo User
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(20))  # Corregido: usar String(20) directamente
    posts: Mapped[list["Post"]] = relationship(back_populates="user")  # Relación con Post

# Definir el modelo Post
class Post(Base):
    __tablename__ = 'posts'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(100))  # Agregar la columna content
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="posts")  # Relación con User

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear un usuario con un post
user = User(name='Zeq Tech', posts=[Post(content="This is some content")])
session.add(user)
session.commit()

# Consultar el usuario y sus posts
user = session.scalar(select(User))
print(f"\nUser {user.id}: {user.name} - Posts: {[post.content for post in user.posts]}\n")