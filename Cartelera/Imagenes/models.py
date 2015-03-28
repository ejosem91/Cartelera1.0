from django.db import models
from Geolocalizacion.models import Geolocalizacion

# Create your model here.
class Imagen(models.Model):
	imagen= models.FileField(upload_to='imagenes/img')
	geo=models.ForeignKey(Geolocalizacion)