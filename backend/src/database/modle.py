from pydantic import BaseModel
from typing import TypeVar, Optional

T = TypeVar('T')

class Ingredient(BaseModel):
    ingredient_name: str
    ingredient_id: str
    base_price: float
    sale_price: float
    discount_amount: float

class Response(BaseModel):
    status: str
    message: str
    code: str
    result: Optional[T] = None