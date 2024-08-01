from django.shortcuts import render

# Create your views here.

def my_function(request):
    return render(request, 'criacao_url/PaginaEmanuel.html')