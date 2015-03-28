from django.db import models
from Ambitos.models import Ambito
from Geolocalizacion.models import Geolocalizacion 

class Portada(models.Model):
	titulo = models.CharField(max_length=30)
	resumen=models.TextField(max_length=140)
	descripcion=models.TextField(max_length=260)
	ambito = models.ForeignKey(Ambito)
	geolocalizacion = models.ForeignKey(Geolocalizacion)
	
def __unicode__(self):
	return self.titulo
