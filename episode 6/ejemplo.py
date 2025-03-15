from time import perf_counter
from sqlalchemy import Column, ForeignKey, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload, subqueryload, selectinload

# Configuración de la base de datos
db_url = 'sqlite:///tecnicas de carga.db'
engine = create_engine(db_url, echo=True)  # Mostrar las consultas SQL en la consola
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship('Post', lazy='select', backref='user')  # cargará los posts de todos los usuarios en una sola consulta adicional usando selectin

    def __repr__(self):
        return f'<User {self.name}>'

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'<Post {self.id}>'

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Insertar datos de ejemplo si no existen
if session.query(User).count() < 1:
    session.add_all(
        [
            User(
                name=f'User {y}',
                posts=[
                    Post(content=f'This is the content for {y * 5 + x}')
                    for x in range(5)
                ],
            )
            for y in range(1_000)  # Crear 1,000 usuarios con 5 posts cada uno
        ]
    )
    session.commit()

print('\n\n')

# Función para medir el tiempo de ejecución de una consulta
def measure_time(description, query_function):
    start = perf_counter()
    result = query_function()
    end = perf_counter()
    print(f'{description}: {end - start:.6f} segundos')
    return result

# Consulta 1: Lazy Loading (carga perezosa)
def lazy_loading_query():
    users = session.query(User).all() # Esto regresa objetos de tipo user, pero los post asociados no se han cargado
    for user in users:
        user.posts  # Acceder a los posts para forzar la carga, resulta ser muy lento
    return users

# Consulta 2: Eager Loading con Joined Load
def joined_load_query():
    users = session.query(User).options(joinedload(User.posts)).all()
    for user in users:
        user.posts  # Los posts ya están cargados
    return users

# Consulta 3: Eager Loading con Subquery Load
def subquery_load_query():
    users = session.query(User).options(subqueryload(User.posts)).all()
    for user in users:
        user.posts  # Los posts ya están cargados
    return users

# Consulta 4: Eager Loading con Select IN Load
def selectin_load_query():
    users = session.query(User).options(selectinload(User.posts)).all()
    for user in users:
        user.posts  # Los posts ya están cargados
    return users

# Medir el tiempo de cada consulta
print("Medición de tiempo para cada tipo de consulta:\n")

# Consulta 1: Lazy Loading
measure_time("Consulta 1: Lazy Loading", lazy_loading_query)

# Consulta 2: Eager Loading con Joined Load
#measure_time("Consulta 2: Eager Loading con Joined Load", joined_load_query)

# Consulta 3: Eager Loading con Subquery Load
#measure_time("Consulta 3: Eager Loading con Subquery Load", subquery_load_query)

# Consulta 4: Eager Loading con Select IN Load
#measure_time("Consulta 4: Eager Loading con Select IN Load", selectin_load_query)