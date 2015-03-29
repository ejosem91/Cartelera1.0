from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Portada

def portada_view(request,titulo):
	cartelera = get_object_or_404(Portada, titulo=titulo)
	return render(request, 'portadas.html',)


# Create your views here.
