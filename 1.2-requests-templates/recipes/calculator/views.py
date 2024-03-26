from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

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
}
def get_recipe(dish: str, request) -> dict:
    servings = int(request.GET.get("servings", 1))
    return {'recipe': {ingredient: count * servings for ingredient, count in DATA.get(dish).items()}, 'servings': servings}

def show_default(request) -> HttpResponse:
    links = {
        'omlet': ["Показать рецепт омлета", reverse("omlet")],
        'pasta': ["Показать рецепт пасты", reverse("pasta")],
        'buter': ["Показать рецепт бутера", reverse("buter")]
    }
    return render(request, "calculator\main.html", links)

def show_omlet(request) -> HttpResponse:
    return render(request, "calculator\index.html", get_recipe('omlet', request))

def show_pasta(request) -> HttpResponse:
    return render(request, "calculator\index.html", get_recipe('pasta', request))

def show_buter(request) -> HttpResponse:
    return render(request, "calculator\index.html", get_recipe('buter', request))