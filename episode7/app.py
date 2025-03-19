from sqlalchemy import BIGINT, String, create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from typing import Optional
from typing_extensions import Annotated
db_url = 'sqlite:///database.db'

engine = create_engine(db_url, echo=True)

#Base = declarative_base()

""" alternativa 1
str_20 = Annotated[str,20]
str_100 = Annotated[str,100]

class Base(DeclarativeBase):
    type_annotation_map = {
        int: BIGINT,
        str_20: String(20),
        str_100: String(100)
        
    }
"""

str_20 = Annotated[Optional[str],mapped_column(String(20))]
str_100 = Annotated[str,mapped_column(String(100))]

class Base(DeclarativeBase):
    pass

class UserLegacy(Base):
    __tablename__ = 'users'
    """
    #id = mapped_column(Integer, primary_key=True)
    #name = mapped_column(String)
    #age = mapped_column(Integer)
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column()
    age: Mapped[int] = mapped_column(nullable=True)
    """
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str_20]
    last_name: Mapped[Optional[str_100]]
    
# create the database tables
Base.metadata.create_all(engine)


"""
type_map: Dict[Type[Any], TypeEngine[Any]] = {
    bool: types.Boolean(),
    bytes: types.LargeBinary(),
    datetime.date: types.Date(),
    datetime.datetime: types.DateTime(),
    datetime.time: types.Time(),
    datetime.timedelta: types.Numeric(),
    float: types.Float(),
    int: types.Integer(),
    str: types.String(),
    uuid.UUID: types.Uuid(),
}
"""