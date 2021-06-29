from django.shortcuts import render, redirect

from recipes.recipes_app.forms import RecipeForm
from recipes.recipes_app.models import RecipeModel


def index(request):
    recipes = RecipeModel.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'GET':
        context = {
            'from': RecipeForm(),
        }
        return render(request, 'create.html', context)
    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'from': form,
        }
        return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = RecipeModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = RecipeForm(initial=recipe.__dict__)
        context = {
            'form': form,
        }
        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'from': form,
        }
        return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = RecipeModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = RecipeForm(initial=recipe.__dict__)
        context = {
            'form': form
        }
        return render(request, 'delete.html', context)
    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe.delete()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'delete.html', context)


def details_recipe(request, pk):
    recipe = RecipeModel.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'details.html', context)
