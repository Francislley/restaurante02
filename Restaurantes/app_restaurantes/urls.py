from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.views.generic import TemplateView
from views import RestauranteList, RestauranteGet, RestauranteUpdate

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
    # Django REST
    url(r'^api/$', views.rest_restaurante, name='rest_restaurante'),
    url(r'^api/(?P<pk>[\d]+)/$', views.rest_element_restaurante,name='rest_element_restaurante'),
    # API REST propia 
    url(r'^api-propia/$', TemplateView.as_view(template_name='api-propia.html')), 
    # Django REST framework APIview
    url(r'^restauranteList/', RestauranteList.as_view(), name='restaurante-list'),
    url(r'^restauranteGet/(?P<pk>[\d])/$', RestauranteGet.as_view(), name='restaurante-get'),
    url(r'^restauranteUpdate/(?P<pk>[\d])/$', RestauranteUpdate.as_view(), name='restaurante-update')
]


