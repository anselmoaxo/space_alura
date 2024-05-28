from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.all()
    contexto = {'cards': fotografias}
    return render(request,  'galeria/index.html', contexto)


def imagem(request, foto_id):
    # get object or 404 busca o id caso não encontre retorno o erro 404
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    contexto = {'fotografia': fotografia}
    return render(request,  'galeria/imagem.html', contexto)