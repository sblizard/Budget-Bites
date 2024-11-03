# builtin
import os

# external
import httpx

# internal
from src.spoonacular.model import GetRecipesInput, Recipes, Recipe


from typing import List

async def get_recipes(input: GetRecipesInput) -> Recipes:
    recipes: List[Recipe] = []  # Define recipes as a list of Recipe models

    # Adjust the loop to limit API requests as needed
    for i in range(20):
        url: str = "https://api.spoonacular.com/recipes/findByIngredients?"

        ingredientsStr = ""

        # Loop through the current batch of ingredients (up to 20)
        for ingredient in input.ingredients[i*20:(i+1)*20]:
            ingredientsStr += f"{ingredient['ingredient_name']},"

        if ingredientsStr:
            url += f"ingredients={ingredientsStr[:-1]}"  # Remove the trailing comma

        url += f"&number={input.number}&ranking={input.ranking}&ignorePantry={input.ignorePantry}&addRecipeInformation=true&addRecipeInstructions=true"

        api_key = "378732fc25a64dd28799e4bafd67abca"

        if api_key:
            url += f"&apiKey={api_key}"

        print(f"Fetching recipes from Spoonacular API: {url}")

        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.get(url)
            data = response.json()
            print("Data from Spoonacular API*****************************:", data)

            # Convert each recipe in data to a Recipe model
            for recipe_data in data:
                recipe = Recipe(**recipe_data)  # Unpack recipe dictionary into Recipe model
                recipes.append(recipe)

    return Recipes(recipes=recipes)  # Return Recipes model containing list of Recipe objects