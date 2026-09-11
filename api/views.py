from django.shortcuts import render
from .models import Categoria
from rest_framework.decorators import api_view

@api_view('GET')
def listar_categorias(request):
    if request.method == 'GET':
        queryset = Categoria.objects.all()
        
    

