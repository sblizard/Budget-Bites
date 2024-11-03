# builtin
from typing import Any, Optional

# external
from pydantic import BaseModel

# internal

class MissedIngredient(BaseModel):
    aisle: Optional[str] = None
    amount: Optional[float] = None
    id: Optional[int] = None
    image: Optional[str] = None
    meta: Optional[list[str]] = None
    name: Optional[str] = None
    original: Optional[str] = None
    originalName: Optional[str] = None
    unit: Optional[str] = None
    unitLong: Optional[str] = None
    unitShort: Optional[str] = None

class UsedIngredients(BaseModel):
    aisle: Optional[str] = None
    amount: Optional[float] = None
    id: Optional[int] = None
    image: Optional[str] = None
    meta: Optional[list[str]] = None
    name: Optional[str] = None
    original: Optional[str] = None
    originalName: Optional[str] = None
    unit: Optional[str] = None
    unitLong: Optional[str] = None
    unitShort: Optional[str] = None

class Recipe(BaseModel):
    id: Optional[int] = None
    image: Optional[str] = None
    imageType: Optional[str] = None
    likes: Optional[int] = None
    missedIngredientCount: Optional[int] = None
    missedIngredients: Optional[list[MissedIngredient]] = None
    title: Optional[str] = None
    unusedIngredients: Optional[list[dict[str, Any]]] = None
    usedIngredientCount: Optional[int] = None
    usedIngredients: Optional[list[UsedIngredients]] = None
    summary: Optional[str] = None
    analyzedInstructions: Optional[list[dict[str, Any]]] = None


class Recipes(BaseModel):
    recipes: Optional[list[Recipe]] = None

class GetRecipesInput(BaseModel):
    ingredients: Optional[list[dict[str, Any]]] = None
    number: Optional[int] = None
    ranking: Optional[int] = None
    ignorePantry: Optional[bool] = None