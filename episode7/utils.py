from typing_extensions import Annotated
from typing import Optional
from sqlalchemy import String, BigInteger, SmallInteger
from sqlalchemy.orm import mapped_column

str_20 = Annotated[str, mapped_column(String(20))]
str_50 = Annotated[str, mapped_column(String(50))]
str_70 = Annotated[str, mapped_column(String(70))]
str_100 = Annotated[Optional[str], mapped_column(String(100))]

int_small = Annotated[SmallInteger, mapped_column(SmallInteger)]
int_big = Annotated[BigInteger, mapped_column(BigInteger)]

from typing_extensions import Annotated
from typing import Optional
from sqlalchemy import String, BigInteger, SmallInteger
from sqlalchemy.orm import mapped_column

# Definiciones de tipos anotados para columnas de texto
str_20 = Annotated[str, mapped_column(String(20))]
str_50 = Annotated[str, mapped_column(String(50))]
str_70 = Annotated[str, mapped_column(String(70))]  # Corregido: usar `str` en lugar de `String(70)`
str_100 = Annotated[Optional[str], mapped_column(String(100))]

# Definiciones de tipos anotados para columnas de enteros
int_small = Annotated[int, mapped_column(SmallInteger)]
int_big = Annotated[int, mapped_column(BigInteger)]