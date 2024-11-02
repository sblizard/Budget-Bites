from pydantic import BaseModel
from typing import TypeVar, Optional

T = TypeVar('T')

class Ingredient(BaseModel):
    ingredient_name: str
    ingredient_id: str
    price: float
    discount: float

class Response(BaseModel):
    status: str
    message: str
    code: str
    result: Optional[T] = None