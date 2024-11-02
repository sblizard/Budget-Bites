# builtin
from contextlib import asynccontextmanager

# external
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

# internal
from src.database.crud import IngredientRepo
from src.database.modle import Ingredient, Response
from src.globals.environment import Environment
from src.database.router import router as database_router
from src.spoonacular.router import router as spoonacular_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    environment: Environment = Environment()
    app.state.environment = environment

    # Initialize the MongoDB client and select the database
    motor_client = AsyncIOMotorClient("mongodb+srv://seanblizard:phDD0Hb0O7s12q3f@mealsforless.yky0i.mongodb.net/?retryWrites=true&w=majority&appName=MealsForLess&ssl_cert_reqs=CERT_NONE")
    app.state.motor = motor_client["ingredients"]  # Use the specific database name here

    yield

    # Close the MongoDB client when done
    motor_client.close()

app: FastAPI = FastAPI(lifespan=lifespan)

app.include_router(database_router)
app.include_router(spoonacular_router)


@app.get('/')
async def root():
    return {'message': 'Hello World!'}
