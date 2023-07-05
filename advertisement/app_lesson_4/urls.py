from django.urls import path, include
from .views import my_func_4

urlpatterns = [
    path('', my_func_4),
]
