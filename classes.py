import datetime
from dataclasses import dataclass

@dataclass
class Product:
  id: str
  parent: str
  title: str # FACT: This typechecking is not implemented at runtime. Use mypy typechecker
  category: str

@dataclass
class Review:
  id: str
  customer_id: str
  stars: int
  headline: str
  body: str
  date: datetime.datetime