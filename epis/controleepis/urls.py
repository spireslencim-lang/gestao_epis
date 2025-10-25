from django.urls import path
from .views import home

urlpatterns = [
    # Cadastrar URLs aqui
    path('', home),

  
]
