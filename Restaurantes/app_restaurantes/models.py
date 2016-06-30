from django.db import models
from mongoengine import *

class Restaurante (models.Model):
    nombre    = models.CharField(max_length=30, unique=True)
    direccion = models.CharField(max_length=60)
    email     = models.EmailField()
    foto     =  models.CharField(max_length=60, blank=True)
    me_gusta  = models.IntegerField(blank=True)
    no_me_gusta  = models.IntegerField()
    id  = models.IntegerField(primary_key=True)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.nombre


connect('tapas')

class Tapa(Document):
    nombre  = StringField(max_length=30)
    foto  =  StringField(max_length=150)
    precio  = IntField(max_length=30)
    nombre_rest = StringField(blank=True)
