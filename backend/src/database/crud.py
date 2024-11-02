import uuid
from src.database.modle import Ingredient
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Request


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