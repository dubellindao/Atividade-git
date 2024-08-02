from urllib import request
from django.shortcuts import render

# Create your views here.

def my_function(request):
    return render(request, 'criacao_url/PaginaLuis.html')