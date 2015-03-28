from django.db import models

class Ambito(models.Model):
	tipo= models.CharField(max_length=25)
	def __unicode__(self):
		return	(self.tipo)

	