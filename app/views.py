from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe

# Create your views here.

def home(request):
    return render (request, 'app/pages/index.html' , context={
        'recipes':[make_recipe() for _ in range(10)],
    })

def recipes(request, id):
    return render (request, 'app/pages/recipe-view.html' , context={
        'recipe':make_recipe()
    })