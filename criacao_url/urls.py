from django.urls import path 
from criacao_url.views import my_function

urlpatterns = [
    path ('', my_function,name='my_function'),
]