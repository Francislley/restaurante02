from rest_framework import serializers
from app_restaurantes.models import Restaurante

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ('id', 'nombre', 'direccion', 'foto', 'me_gusta')


