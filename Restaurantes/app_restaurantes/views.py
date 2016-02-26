from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def hola_funcion (request):
    return HttpResponse("Hola mundo")


def index (request):
	context= {'mensaje': 'restaurantes!',}
	return render (request, 'base.html', context)
