from django.shortcuts import render
#nuevas librerias
from django.http import HttpResponse
from .models import *


# Create your views here.

def index(request):
    noticias = Noticias.objects.all()
    
    return render(request, 'noticias/index.html')