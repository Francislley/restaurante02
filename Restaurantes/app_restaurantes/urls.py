from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # para /app_restaurante/index
    url(r'^index$', views.index, name='index'),
    # para /app_restaurante/otro_url
    url(r'^hola$', views.hola_funcion, name='hola_funcion'),

]

