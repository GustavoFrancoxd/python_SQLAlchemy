from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# group users by age
"""
# SELECT age FROM users GROUP BY age;
users = session.query(User.age).group_by(User.age).all()
print(users)
"""

# group users by age
"""
# SELECT age, COUNT(id) FROM users GROUP BY age;
users = session.query(User.age, func.count(User.id)).group_by(User.age).all()
print(users)
"""

# group users by name
"""
# SELECT name, COUNT(id) FROM users GROUP BY name;
users = session.query(User.name, func.count(User.id)).group_by(User.name).all()
print(users)
"""

# chaining
"""
#users = session.query(User).filter(User.age > 24).filter(User.age < 50).all()
users = session.query(User.name, User.age).filter(User.age > 24, User.age < 50).all()
print(users)
"""

# tuples
"""
# SELECT age, COUNT(id) FROM users WHERE age >24 AND age < 50 GROUP BY age ORDER BY "age" 
users_tuple = (
    session.query(User.age, func.count(User.id))
    .filter(User.age > 24)
    .order_by(User.age)
    .filter(User.age < 50)
    .group_by(User.age)
    .all()
)

for age, count in users_tuple:
    print(f"Age: {age} - {count} users")
"""

only_iron_man = True
group_by_age = True

users = session.query(User)

if only_iron_man:
    users = users.filter(User.name == "Iron man")
    
if group_by_age:
    users = users.group_by(User.age)

users = users.all()

for user in users:
    print(f"User age: {user.age}, name: {user.name}")