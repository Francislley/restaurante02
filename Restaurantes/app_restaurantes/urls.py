from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # para /app_restaurante/index
    url(r'^index$', views.index, name='index'),
    # para /app_restaurante/hola
    url(r'^hola$', views.hola_funcion, name='hola_funcion'),
    # para /app_restaurante/ 
    url(r'^$', views.index, name='index'),
    # para aniadir voto
    url(r'^like_category/$', views.like_category, name='like_category'),
    # para aniadir voto negativo (dislike)
    url(r'^dislike_category/$', views.dislike_category, name='dislike_category'),
    # para recoger el formulario de las tapas
    url(r'^at/$', views.add_tapa, name ='add_tapa'),

]

