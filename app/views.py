from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return HttpResponse('Página de contato')

def about(request):
    return HttpResponse('Página de Sobre')
