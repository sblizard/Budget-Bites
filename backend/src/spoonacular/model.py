# builtin

# external
from pydantic import BaseModel

# internal


class MissedIngredient(BaseModel):
    aisle: str
    amount: float
    id: int
    image: str
    meta: list[str]
    name: str
    original: str
    originalName: str
    unit: str
    unitLong: str
    unitShort: str

class UsedIngredients(BaseModel):
    aisle: str
    amount: float
    id: int
    image: str
    meta: list[str]
    name: str
    original: str
    originalName: str
    unit: str
    unitLong: str
    unitShort: str

class Recipe(BaseModel):
    id: int
    image: str
    imageType: str
    likes: int
    missedIngredientCount: int
    missedIngredients: list[MissedIngredient]
    title: str
    unusedIngredients: list[str]
    usedIngredientCount: int
    usedIngredients: list[UsedIngredients]

class Recipes(BaseModel):
    recipes: list[Recipe]

class GetIngredientsInput(BaseModel):
    ingredients: list[str]
    number: int
    ranking: int
    ignorePantry: bool