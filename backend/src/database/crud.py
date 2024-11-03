import uuid
from src.database.modle import Ingredient
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Request, HTTPException
from src.spoonacular.model import Recipe
from pydantic import BaseModel
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

def serialize_objectid(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    return obj


class IngredientRepo():

    @staticmethod
    async def retrieve_ingredients(request: Request):
        _ingredient = []
        motor_db = request.app.state.motor 
        collection = motor_db.get_collection("Ingredients")
        async for ingredient in collection.find():
            _ingredient.append(ingredient)
        return _ingredient


    @staticmethod
    async def insert_ingredient(ingredient: Ingredient, request: Request):
        id = str(uuid.uuid4())
        motor: AsyncIOMotorClient = request.app.state.motor
        _ingredient = {
            "ingredient_name": ingredient.ingredient_name,
            "ingredient_id": id,
            "sale_price": ingredient.sale_price,
            "base_price": ingredient.base_price,
            "discount": ingredient.discount_amount
        }
        await motor.get_collection('Ingredients').insert_one(_ingredient)


    @staticmethod
    async def update_ingredient(ingredient_id: str, ingredient: Ingredient, request: Request):
        motor: AsyncIOMotorClient = request.app.state.motor
        _ingredient = await motor.database.get_collection('ingredients').find_one({"ingredient_id": ingredient_id})
        _ingredient['ingredient_name'] = ingredient.ingredient_name
        _ingredient['price'] = ingredient.price
        _ingredient['discount'] = ingredient.discount
        await motor.get_collection('Ingredients').update_one({"ingredient_id": ingredient_id}, {"$set": _ingredient})


    @staticmethod
    async def delete_ingredient(ingredient_id: str, request: Request):
        motor: AsyncIOMotorClient = request.app.state.motor
        await motor.get_collection('Ingredients').delete_one({"ingredient_id": ingredient_id})


    @staticmethod
    async def retrieve_ingredient_by_id(ingredient_id: str, request: Request):
        motor: AsyncIOMotorClient = request.app.state.motor
        _ingredient = await motor.get_collection('Ingredients').find_one({"ingredient_id": ingredient_id})
        return _ingredient
    


class RecipeRepo():

    @staticmethod
    async def retrieve_recipes(request: Request):
        _recipes = []
        motor_db = request.app.state.recipe_motor 
        collection = motor_db.get_collection("Recipes")  
        async for recipe in collection.find():
            recipe['_id'] = str(recipe['_id'])  # Convert ObjectId to string
            _recipes.append(recipe)
        return _recipes


    @staticmethod
    async def insert_recipe(recipe: Recipe, request: Request):
        id = str(uuid.uuid4())
        motor: AsyncIOMotorClient = request.app.state.recipe_motor

        # Adjust unusedIngredients to handle dictionaries or Pydantic models
        _recipe = {
            "id": id,
            "image": recipe.image,
            "imageType": recipe.imageType,
            "likes": recipe.likes,
            "missedIngredientCount": recipe.missedIngredientCount,
            "missedIngredients": [ingredient.dict() if isinstance(ingredient, BaseModel) else ingredient for ingredient in recipe.missedIngredients or []],
            "title": recipe.title,
            "unusedIngredients": [ingredient if isinstance(ingredient, dict) else ingredient.dict() for ingredient in recipe.unusedIngredients or []],
            "usedIngredients": [ingredient.dict() if isinstance(ingredient, BaseModel) else ingredient for ingredient in recipe.usedIngredients or []],
            "usedIngredientCount": recipe.usedIngredientCount,
            "summary": recipe.summary,
            "analyzedInstructions": recipe.analyzedInstructions
        }

        await motor.get_collection('Recipes').insert_one(_recipe)


    @staticmethod
    async def update_recipe(recipe_id: str, recipe: Recipe, request: Request):
        motor: AsyncIOMotorClient = request.app.state.recipe_motor
        collection = motor.database.get_collection('recipes')

        existing_recipe = await collection.find_one({"id": recipe_id})
        if not existing_recipe:
           raise HTTPException(status_code=404, detail="Recipe not found")

        _recipe = {
            "id": recipe_id,  # Ensure the ID is preserved
            "image": recipe.image,
            "imageType": recipe.imageType,
            "likes": recipe.likes,
            "missedIngredientCount": recipe.missedIngredientCount,
            "missedIngredients": recipe.missedIngredients,
            "title": recipe.title,
            "unusedIngredients": recipe.unusedIngredients,
            "usedIngredients": recipe.usedIngredients,
            "usedIngredientCount": recipe.usedIngredientCount,
            "summary": recipe.summary,
            "analyzedInstructions": recipe.analyzedInstructions
        }

        update_data = {k: v for k, v in _recipe.items() if v is not None}

        await collection.update_one({"id": recipe_id}, {"$set": update_data})

    @staticmethod
    async def delete_recipe(recipe_id: str, request: Request):
        motor: AsyncIOMotorClient = request.app.state.recipe_motor
        await motor.get_collection('Recipes').delete_one({"recipe_id": recipe_id})



    @staticmethod
    async def retrieve_recipe_by_id(recipe_id: str, request: Request):
        motor: AsyncIOMotorClient = request.app.state.recipe_motor
        try:
            id = ObjectId(recipe_id)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid recipe ID format")
        
        _recipe = await motor.get_collection('Recipes').find_one({"_id": id})
        if not _recipe:
            raise HTTPException(status_code=404, detail="Recipe not found")
        
        _recipe['_id'] = str(_recipe['_id'])  # Convert ObjectId to string
        serialized_recipe = jsonable_encoder(_recipe)  # Ensure all fields are JSON serializable
        return serialized_recipe