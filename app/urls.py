from django.urls import path
from app.views import contact, home, about

urlpatterns = [
    path('', home),
    path('contato/', contact),
    path('sobre/', about)
]
