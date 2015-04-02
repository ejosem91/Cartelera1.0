from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from .models import Portada,Geolocalizacion
from Imagenes.models import Imagen


def portada_view(request, titulo):

	portada= get_object_or_404(Portada, titulo=titulo)
	geo= portada.geolocalizacion
	nombre_img=Imagen.objects.values("imagen").get(geo=geo)
	#nombre_img=get_object_or_404(Imagen,'imagen').get(geo=geo)

	
	return render(request,'portadas.html', {'portada':portada,'geo':geo,'nombre_img':nombre_img})


# Create your views here.
