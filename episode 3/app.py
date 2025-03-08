from models import Address, session, User

#creating users: se crean los objetos usuarios
user1 = User(name="John Doe", age=52)
user2 = User(name="Jane Smith", age=34)

# Creating addresses with users: se crean los objetos direccion
address1 = Address(city="New York", state="NY", zip_code="10001")
address2 = Address(city="Los Angeles", state="CA", zip_code="90001")
address3 = Address(city="Chicago", state="IL", zip_code="60601")

# Associating addresses with users: asociamos cada objeto usuario con sus direcciones
user1.addresses.extend([address1, address2])
user2.addresses.append(address3)

# Adding users and addresses to the session and committing changes to the database: se abre la sesion y agregan los elementos a la base de datos
session.add(user1)
session.add(user2)
session.commit()

# visualizamos la informacion de los objetos creados
print(f"{user1.addresses = }")  # el simbolo igual permite ver el nombre de la propiedad o metodo, y el resultado de este
print(f"{user2.addresses = }")
print(f"{address1.user = }")