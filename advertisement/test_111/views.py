from django.shortcuts import render
from django.http import HttpResponse


def my_func(request):
    return HttpResponse('Возвращение ответа!!')
