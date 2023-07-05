from django.urls import path, include
from .views import my_func

urlpatterns = [
    path('', my_func),
]
