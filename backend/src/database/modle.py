from pydantic import BaseModel
from typing import TypeVar, Optional

T = TypeVar('T')

class Ingredient(BaseModel):
    ingredient_name: Optional[str] = None
    ingredient_id: Optional[str] = None
    base_price: Optional[float] = None
    sale_price: Optional[float] = None
    discount_amount: Optional[float] = None

class Response(BaseModel):
    status: Optional[str] = None
    message: Optional[str] = None
    code: Optional[str] = None
    result: Optional[T] = None