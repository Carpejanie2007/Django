from django.urls import path
from .views import listar_categoria

urlpatterns = [
    path('categorias', listar_categoria)
]