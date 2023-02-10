from django.shortcuts import render, get_object_or_404
#nuevas librerias
from django.http import HttpResponse
from .models import *


# Create your views here.

def index(request):
    question = get_object_or_404
    noticias = Noticias.objects.get()
    
    return render(request, 'noticiario/index.html',{
        'noticiasTemplate': get_object_or_404(Noticias),
    })