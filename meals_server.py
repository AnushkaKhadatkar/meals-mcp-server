from mcp.server.fastmcp import FastMCP
import requests
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

mcp = FastMCP("meals")
server = mcp

BASE_URL = "https://www.themealdb.com/api/json/v1/1"


@mcp.tool()
def search_meals_by_name(query: str, limit: int = 5):
    response = requests.get(
        f"{BASE_URL}/search.php",
        params={"s": query}
    )
    response.raise_for_status()
    data = response.json()

    meals = data.get("meals")
    if not meals:
        return {"message": "no matches", "results": []}

    results = []
    for meal in meals[:limit]:
        results.append({
            "id": meal["idMeal"],
            "name": meal["strMeal"],
            "area": meal["strArea"],
            "category": meal["strCategory"],
            "thumb": meal["strMealThumb"]
        })

    return results


@mcp.tool()
def meals_by_ingredient(ingredient: str, limit: int = 12):
    response = requests.get(
        f"{BASE_URL}/filter.php",
        params={"i": ingredient}
    )
    response.raise_for_status()
    data = response.json()

    meals = data.get("meals")
    if not meals:
        return {"message": "no matches", "results": []}

    return [
        {
            "id": meal["idMeal"],
            "name": meal["strMeal"],
            "thumb": meal["strMealThumb"]
        }
        for meal in meals[:limit]
    ]


@mcp.tool()
def meal_details(meal_id: str):
    response = requests.get(
        f"{BASE_URL}/lookup.php",
        params={"i": meal_id}
    )
    response.raise_for_status()
    data = response.json()

    meals = data.get("meals")
    if not meals:
        return {"message": "no matches"}

    meal = meals[0]

    ingredients = []
    for i in range(1, 21):
        ingredient = meal.get(f"strIngredient{i}")
        measure = meal.get(f"strMeasure{i}")
        if ingredient and ingredient.strip():
            ingredients.append({
                "name": ingredient,
                "measure": measure
            })

    return {
        "id": meal["idMeal"],
        "name": meal["strMeal"],
        "category": meal["strCategory"],
        "area": meal["strArea"],
        "instructions": meal["strInstructions"],
        "image": meal["strMealThumb"],
        "source": meal["strSource"],
        "youtube": meal["strYoutube"],
        "ingredients": ingredients
    }


@mcp.tool()
def random_meal():
    response = requests.get(f"{BASE_URL}/random.php")
    response.raise_for_status()
    data = response.json()

    meal = data["meals"][0]

    ingredients = []
    for i in range(1, 21):
        ingredient = meal.get(f"strIngredient{i}")
        measure = meal.get(f"strMeasure{i}")
        if ingredient and ingredient.strip():
            ingredients.append({
                "name": ingredient,
                "measure": measure
            })

    return {
        "id": meal["idMeal"],
        "name": meal["strMeal"],
        "category": meal["strCategory"],
        "area": meal["strArea"],
        "instructions": meal["strInstructions"],
        "image": meal["strMealThumb"],
        "source": meal["strSource"],
        "youtube": meal["strYoutube"],
        "ingredients": ingredients
    }


if __name__ == "__main__":
    mcp.run()