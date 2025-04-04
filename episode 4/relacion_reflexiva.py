from sqlalchemy import Column, ForeignKey, Integer, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = 'sqlite:///ep_07_one_to_one_self_relationships.db'

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Node(Base):
    __tablename__ = 'nodes'

    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)

    node_id = Column(Integer, ForeignKey('nodes.id')) #Columna de clave foránea que apunta al id de otra fila en la misma tabla
    next_node = relationship('Node', remote_side=[id], uselist=False, post_update=True)
    """ La opción remote_side=[id] indica que la relación es autorreferencial. uselist=False asegura que la
    relación es uno a uno (en lugar de uno a muchos). post_update=True permite que la relación se actualice 
    después de que se haya creado la fila."""

    def __repr__(self):
        return f'<Node {self.id} value={self.value}, next node id={self.next_node.id}>'


Base.metadata.create_all(engine)

# If there is data in the database, dont add more data
if session.query(Node).count() < 1:
    node1 = Node(value=1)
    node2 = Node(value=2)
    node3 = Node(value=3)

    node1.next_node = node2
    node2.next_node = node3
    node3.next_node = node1

    session.add_all([node1, node2, node3])
    session.commit()


node1, node2, node3 = session.query(Node).limit(3).all()

print(node1)
print(node2)
print(node3)