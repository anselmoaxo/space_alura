from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms()
    contexto = {
        'form': form
    }
    return render(request, 'usuarios/login.html', contexto)

    
def cadastro(request):
    form = CadastroForms()
    contexto = {
        'form': form
    }
    return render(request, 'usuarios/cadastro.html', contexto)
