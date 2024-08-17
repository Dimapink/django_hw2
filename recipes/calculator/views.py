from django.core.exceptions import SuspiciousOperation
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def receipt(request, dish):
    multiplayer = request.GET.get("servings")
    recipe = DATA.get(dish)
    if multiplayer:
        multiplayer = float(multiplayer)
        if multiplayer <= 0:
            raise SuspiciousOperation("Количество блюд не должно быть меньше 0")
        recipe = {k: v*multiplayer for k, v in recipe.items()}
    context = {"recipe": recipe}
    return render(request, "calculator/index.html", context)
