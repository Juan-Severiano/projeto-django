from django.urls import path
from app import views


app = 'receitas'

urlpatterns = [
    path('', views.home, name="receitas-home"),
    path('recipes/<int:id>/', views.recipes, name="receitas-receitas")
]