from django.urls import path
from .views import listar_categoria
from .views import listar_produtos

urlpatterns = [
    path('categorias/', listar_categoria),
    path('produtos/',listar_produtos)
]