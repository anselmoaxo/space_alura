from django.shortcuts import render
from usuarios.forms import LoginForms

def login(request):
    form = LoginForms()
    contexto = {
        'form': form
    }
    return render(request, 'usuarios/login.html', contexto)

    
def cadastro(request):
    return render(request, 'usuarios/cadastro.html')
