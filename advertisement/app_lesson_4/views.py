from django.shortcuts import render
from django.http import HttpResponse


def my_func_4(request):
    return HttpResponse('Домашка по 4 занятию')
