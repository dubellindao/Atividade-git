from django.urls import path 
from criacao_url.views import my_function_luis, my_function_emanuel

urlpatterns = [
    path ('', my_function_luis,name='my_function-luis'),
    path('emanuel/', my_function_emanuel,name='my_function-emanuel'),
]