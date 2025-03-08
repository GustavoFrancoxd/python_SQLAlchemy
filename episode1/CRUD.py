
from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

# De esta forma se insertan usuarios
"""
user = User(name="John Doe", age=30)
user_2 = User(name = "Andrew pip", age=25)
user_3 = User(name="Iron man", age=57)
user_4 = User(name="Richard Rodriguez", age=25)
session.add(user_2)
session.add_all([user_3, user_4])

session.commit()
"""


# De esta forma se pueden recuperar los datos de los usuarios
"""
users = session.query(User).all()

user = users[0]
print(user)
print(user.id)
print(user.name)
print(user.age)

for user in users:
    print(f"User id: {user.id}, name: {user.name}, age: {user.age}" )
"""


#de esta manera podemos buscar un elemento con un atributo unico como el id
"""
user = session.query(User).filter_by(id=1).one_or_none()

print(user)
print(user.id)
print(user.name)
print(user.age)
"""

# Hacer busquedas
"""
users = session.query(User).filter_by(age=25).all()
#print(users)
for user in users:
    print(f"User id: {user.id}, name: {user.name}, age: {user.age}" )
    
# Obtener primer resultado
user = session.query(User).filter_by(age=25).first()
print(user)
print(user.id)
print(user.name)
print(user.age)
"""


# hacer modificaciones 
"""
user = session.query(User).filter_by(id=1).one_or_none()
print(user.name)

user.name = "A different name"
print(user.name)

session.commit()
"""


# Hacer eliminaciones
"""
user = session.query(User).filter_by(id=1).one_or_none()
session.delete(user)
session.commit()
"""
