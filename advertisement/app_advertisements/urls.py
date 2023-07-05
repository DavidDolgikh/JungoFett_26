from django.urls import path
from .views import index

urlpatterns = [         # обязательно, зарезервированное имя, которое фреймворк будет искать
    path('', index)     # эта функция формирует пути (связывать путь с представлением (корневым адресом))
]