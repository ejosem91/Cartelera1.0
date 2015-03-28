from django.db import models

# Create your models here.
class Geolocalizacion(models.Model):
	lugar=models.CharField(max_length=30)
	latitud=models.DecimalField(max_digits=10, decimal_places=7)
	longitud=models.DecimalField(max_digits=10, decimal_places=7)
	
	def __unicode__(self):
		return self.lugar
