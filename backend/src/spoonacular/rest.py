# builtin
import os

# external
import httpx

# internal
from src.spoonacular.model import GetIngredientsInput, Recipes


async def get_recipes(input: GetIngredientsInput) -> Recipes:
    url = "https://api.spoonacular.com/recipes/findByIngredients?"

    if len(input.ingredients) > 0:
        url += "ingredients="

        for ingredient in input.ingredients:
            url += f"{ingredient},"
        url = url[:-1]

    url += f"&number={input.number}&ranking={input.ranking}&ignorePantry={input.ignorePantry}"


    api_key: str = "57006aca24614a3e9fc6d1b4a7ee673a"

    print(f"API Key: {api_key}")

    if api_key is not None:
        url += f"&apiKey={api_key}"

    print(f"Fetching recipes from Spoonacular API: {url}")

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        print(response)
        
        if response.status_code == 200:
            data = response.json()
            return Recipes(recipes=data)
        else:
            error_data = response.json()
            print("Error from Spoonacular API:", error_data)
            raise ValueError("Failed to fetch recipes from Spoonacular API")