import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Restaurantes.settings')

import django
django.setup()

from app_restaurantes.models import Restaurante


def populate():

	p = Restaurante (nombre="Torrepalma", direccion="C/ Conde de Torrepalma", email="preguntas@hoteltorrepalma.com", foto="http://bit.ly/1pxXa6K")
	p.save()

	q = Restaurante (nombre="Meson El Barrio", direccion="calle 234", email="correo2@correo.com", foto="http://www.reservamesa.com/fotos/restaurantes/4490_5.jpg")
	q.save()

	r = Restaurante (nombre="Via Priego", direccion="Carretera de Priego km. 100", email="info@caserioviapriego.com", foto="http://caserioviapriego.com/fotoentradasalon.jpg")
	r.save()

	t = Restaurante (nombre="Cafe El Vecino", direccion="calle 456", email="correo4@correo.com", foto="https://s-media-cache-ak0.pinimg.com/736x/74/5c/9a/745c9af2c6222f40403fcbb5e4d2c2c6.jpg")
	t.save()

	v = Restaurante (nombre="Cafe-Bar Europa", direccion="Avenida Europa 13", email="correo5@correo.com", foto="http://blogs.antena3.com/clipping/2014/05/22/00573/31.jpg")
	v.save()

	# muestro el nombre de los restaurantes para comprobarlo
	for c in Restaurante.objects.all():
            print "- {0}".format(str(c))

	return 0


if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
