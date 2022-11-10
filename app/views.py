from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render (request, 'app/pages/index.html' , context={
        'name':'Juan Severiano'
    })

def recipes(request, id):
    return render (request, 'app/pages/recipe-view.html' , context={
        'name':'Juan Severiano'
    })