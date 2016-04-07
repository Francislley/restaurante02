from django.shortcuts import render
from django.http import HttpResponse
from app_restaurantes.models import Restaurante
from django.contrib.auth.decorators import login_required


def hola_funcion (request):
    return HttpResponse("Hola mundo")


def index (request):
	lista = Restaurante.objects.all()
	context= {'mensaje': 'restaurantes!', 'restaurante': lista[:4]} #paso los 4 primeros solo
	return render (request, 'base.html', context)


@login_required
def like_category(request):
	cat_id = None
	if request.method == 'GET':
        	cat_id = request.GET.get('me_gusta','')	
	likes = 0
	if cat_id:
		cat = Restaurante.objects.get(id=cat_id)
	if cat:
		likes = cat.me_gusta + 1
		cat.me_gusta =  likes
		cat.save()



	return HttpResponse(likes)


@login_required
def dislike_category(request):
	cat_id = None
	if request.method == 'GET':
        	cat_id = request.GET.get('no_me_gusta','')
	dislikes = 0
	if cat_id:
		cat = Restaurante.objects.get(id=cat_id)
	if cat:
		dislikes = cat.no_me_gusta + 1
		cat.no_me_gusta =  dislikes
		cat.save()



	return HttpResponse(dislikes)

