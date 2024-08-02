from urllib import request
from django.shortcuts import render

# Create your views here.

def my_function_luis(request):
    return render(request, 'criacao_url/PaginaLuis.html')

def my_function_emanuel(request):
    return render(request, 'criacao_url/PaginaEmanuel.html')