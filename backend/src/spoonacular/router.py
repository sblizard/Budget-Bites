# builtin

# external
from fastapi import APIRouter

# internal
from src.spoonacular.rest import get_recipes
from src.spoonacular.model import GetIngredientsInput, Recipes

router: APIRouter = APIRouter()

@router.get("/recipes")
async def get_recipes_endpoint(input: GetIngredientsInput) -> Recipes:
    return await get_recipes(input)