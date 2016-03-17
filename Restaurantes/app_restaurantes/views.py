from django.shortcuts import render
from django.http import HttpResponse
from app_restaurantes.models import Restaurante

def hola_funcion (request):
    return HttpResponse("Hola mundo")


def index (request):
	lista = Restaurante.objects.all()
	context= {'mensaje': 'restaurantes!', 'restaurante': lista[:4]} #paso los 4 primeros solo
	return render (request, 'base.html', context)
