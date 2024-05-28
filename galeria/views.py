from django.shortcuts import render
from galeria.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.all()
    contexto = {'cards': fotografias}
    return render(request,  'galeria/index.html', contexto)


def imagem(request):
    
    return render(request,  'galeria/imagem.html')