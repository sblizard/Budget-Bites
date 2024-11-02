from fastapi import APIRouter, Request
from src.database.crud import IngredientRepo
from src.database.modle import Ingredient, Response
from motor.motor_asyncio import AsyncIOMotorClient


router = APIRouter()


@router.get('/ingredient/')
async def retrieve_ingredients(request: Request):
    ingredients = await IngredientRepo.retrieve_ingredients(request=request)
    return Response(status="success", message="Ingredients retrieved successfully", code="200", result=ingredients)


@router.post('/ingredient/create')
async def create_ingredient(request: Request, ingredient: Ingredient):
    motor: AsyncIOMotorClient = request.app.state.motor
    await IngredientRepo.insert_ingredient(ingredient, request=request)
    return Response(status="success", message="Ingredient created successfully", code="201")


@router.get('/ingredient/{ingredient_id}')
async def retrieve_ingredient_by_id(ingredient_id: str, request: Request):
    ingredient = await IngredientRepo.retrieve_ingredient_by_id(ingredient_id, request=request)
    return Response(status="success", message="Ingredient retrieved successfully", code="200", result=ingredient)


@router.post('/ingredient/update/{ingredient_id}')
async def update_ingredient(ingredient_id: str, ingredient: Ingredient, request: Request):
    await IngredientRepo.update_ingredient(ingredient_id, ingredient, request)
    return Response(status="success", message="Ingredient updated successfully", code="200")


@router.delete('/ingredient/delete/{ingredient_id}')
async def delete_ingredient(ingredient_id: str, request: Request):
    await IngredientRepo.delete_ingredient(ingredient_id, request)
    return Response(status="success", message="Ingredient deleted successfully", code="200")