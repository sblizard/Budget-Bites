# builtin

# external
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse


# internal
from src.spoonacular.rest import get_recipes
from src.spoonacular.model import GetRecipesInput, Recipes
from src.database.crud import RecipeRepo

router: APIRouter = APIRouter()

@router.get("/recipes")
async def get_recipes_endpoint(input: GetRecipesInput) -> Recipes:
    return await get_recipes(input)
    
@router.get("/all-recipes")
async def get_all_recipes(request: Request):
    recipes = await RecipeRepo.retrieve_recipes(request=request)
    return JSONResponse(content=recipes)