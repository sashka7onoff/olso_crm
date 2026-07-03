from django.shortcuts import render
from django.shortcuts import HttpResponse


def index_shop(request):
    return HttpResponse("Hola from shop! :)")
