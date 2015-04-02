from django.contrib import admin
from models import Ambito

class AdminAmbito(admin.ModelAdmin):
	list_display= ('tipo',)
	list_filter=('tipo',)
	search_fields=('tipo',)


admin.site.register(Ambito, AdminAmbito)
