from sqlalchemy import BIGINT, String, create_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from typing import Optional
from typing_extensions import Annotated
from utils import str_100, str_20


db_url = 'sqlite:///database.db'


engine = create_engine(db_url, echo=True)

class Base(DeclarativeBase):
    pass

class UserLegacy(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str_20]
    last_name: Mapped[Optional[str_100]]
    
# create the database tables
Base.metadata.create_all(engine)

