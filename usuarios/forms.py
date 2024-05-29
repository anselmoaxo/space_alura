from django.forms import forms


class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label= 'Nome de Login',
        max_length=50, 
        required=True)
    senha = forms.Charfiled(
        label= 'Senha',
        max_length=57, 
        Widget= forms.PasswordInput()
        required=True)

    
