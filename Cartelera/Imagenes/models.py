from django.db import models
from Geolocalizacion.models import Geolocalizacion

# Create your model here.
class Imagen(models.Model):
	nombre= models.CharField(max_length=30)
	imagen= models.FileField(upload_to='imagenes/img')
	geo=models.ForeignKey(Geolocalizacion)

	def __unicode__(self):
		return self.nombre 
	
		