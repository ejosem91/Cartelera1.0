from django.contrib import admin
from models import Portada
from actions import export_as_excel

class AdminPortadas(admin.ModelAdmin):
	list_display=('titulo','ambito','geolocalizacion')
	search_fields=('titulo','ambito','geolocalizacion')
	list_editable=['ambito',]
	actions=(export_as_excel,)
admin.site.register(Portada,AdminPortadas)
# Register your models here.
