from django.urls import path
from .views import index, top_sellers
from .views import index, advertisement_post

urlpatterns = [         # обязательно, зарезервированное имя, которое фреймворк будет искать
    path('', index, name='main-page'),     # эта функция формирует пути (связывать путь с представлением (корневым адресом))
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name='adv-post'),
]