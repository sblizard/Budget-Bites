# builtin
from contextlib import asynccontextmanager

# external
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

# internal
from src.database.crud import IngredientRepo, RecipeRepo
from src.database.modle import Ingredient, Response
from src.globals.environment import Environment
from src.database.router import router as database_router
from src.spoonacular.router import router as spoonacular_router
from src.spoonacular.model import GetRecipesInput, Recipes
from src.spoonacular.rest import get_recipes

@asynccontextmanager
async def lifespan(app: FastAPI):
    environment: Environment = Environment()
    app.state.environment = environment

    # Initialize the MongoDB client and select the database
    motor_client = AsyncIOMotorClient("mongodb+srv://seanblizard:phDD0Hb0O7s12q3f@mealsforless.yky0i.mongodb.net/?retryWrites=true&w=majority&appName=MealsForLess&ssl_cert_reqs=CERT_NONE")
    app.state.motor = motor_client["ingredients"] 
    app.state.recipe_motor = motor_client["recipes"]

    yield

    # Close the MongoDB client when done
    motor_client.close()

app: FastAPI = FastAPI(lifespan=lifespan)

# Configure CORS
origins = [
    "http://localhost:3000",  # Your frontend's origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(database_router)
app.include_router(spoonacular_router)


@app.get('/')
async def root():
    return {'message': 'Hello World!'}

@app.get("/make-recipes")
async def makeRecipes(request: Request):
    ingridents: list[str] = await IngredientRepo.retrieve_ingredients(request=request)

    print(f'***************************ingredients:{ingridents}***************************')


    getRecipesInput: GetRecipesInput = GetRecipesInput(ingredients=ingridents, number=5, ranking=2, ignorePantry=True)

    recipes: Recipes = await get_recipes(getRecipesInput)

    for recipe in recipes.recipes:
        await RecipeRepo.insert_recipe(recipe=recipe, request=request)
        print(f'**********************RECIPE HERE*******: {recipe}')

    return Response(message="Recipes made successfully", data=recipes)