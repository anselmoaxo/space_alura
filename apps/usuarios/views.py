from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForms()
    
    if request.method =='POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            username = request.POST.get('nome_login')
            senha = request.POST.get('senha')
        usuario = auth.authenticate(
            request,
            username=username,
            password=senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{username} , Logado com Sucesso! ')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao Efetuar Login , Tente novamente!')
            return redirect('login')
       

    return render(request, 'usuarios/login.html', {'form': form})

    
def cadastro(request):
    form = CadastroForms()
    #Verifica se a requisição HTTP é do tipo POST, o que indica que o formulário foi submetido.
    if request.method =='POST':
        form = CadastroForms(request.POST)

        #Verifica se os dados do formulário são válidos de acordo com as regras definidas na classe do formulário
        if form.is_valid():
            
            
            nome = request.POST.get('nome_cadastro')
            email = request.POST.get('email')
            senha = request.POST.get('password1')

            #Verifica se já existe um usuário com o mesmo nome de usuário. Se existir, redireciona de volta para a página de cadastro.
            if User.objects.filter(username=nome).exists():
                messages.error(request, f'Erro , Cadastro {nome} já existe')
                return redirect('cadastro')
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro realizado com Sucesso ')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {
        'form': form
    })


def logout(request):
    auth.logout(request)
    messages.success(request,'Logout, Efetuado com Sucesso')
    return redirect('login')