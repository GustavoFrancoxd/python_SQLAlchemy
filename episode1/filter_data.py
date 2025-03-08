from sqlalchemy import or_, and_, not_
from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

"""# query all users
users_all = session.query(User).all()

# query all users with age greater than or equal to 25
users_filtered = session.query(User).filter(User.age >= 25, User.name == "Iron man").all()

print("all users:", len(users_all))
print("Filtered Users:", len(users_filtered))"""


# el metodo filter_by no funciona con condicionales
"""
users_all = session.query(User).all()

users_filtered = session.query(User).filter_by(age=25).all()

for user in users_filtered:
    print(f"User age: {user.id}, name: {user.name}, age: {user.age}" )
"""

# metodo where
"""
users = session.query(User).where( (User.age >= 30) | (User.name == "Iron Man") | (User.id > 4) ).all()
#users = session.query(User).where(or_(User.age >= 30, User.name == "Iron Man", User.id > 4)).all()

#users = session.query(User).where( (User.age >= 30) & (User.name == "Iron Man") & (User.id > 4) ).all()
#users = session.query(User).where(and_(User.age >= 30, User.name == "Iron Man", User.id > 4)).all()

#users = session.query(User).where( not_(User.name == "Iron Man")).all()
#users = session.query(User).where(or_(User.age >= 30, User.name == "Iron Man", User.id > 4)).all()

for user in users:
    print(f"User age: {user.id}, name: {user.name}, age: {user.age}" )
"""

# SELECT * FROM users WHERE name != "Iron man" OR age > 35 AND age < 60
users =(
    session.query(User).where(
        or_(
            not_(User.name == "Iron man"),
            and_(
                User.age > 35,
                User.age < 60
            )
        )
    )
)