import random
from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)

Session= sessionmaker(bind=engine)
session = Session()

# Crear datos
"""
names = ["Andrew Pip", "Iron man", "John Doe", "Jane Doe"]
ages = [20, 21, 22, 23, 25, 27, 30, 35, 60]

for x in range(20):
    session.add(
        User(name=random.choice(names), age= random.choice(ages))
    )
    
session.commit()
"""

# Ordenar informacion 
users = session.query(User).order_by(User.age.desc(), User.name).all()

for user in users:
    print(f"User id: {user.id}, name: {user.name}, age: {user.age}" )