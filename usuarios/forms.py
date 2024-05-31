from django import forms


class LoginForms(forms.Form):
    nome_login=forms.CharField(label= 'Nome de Login',
                                 max_length=50, 
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={
                                    "class": "form-control",
                                     "placeholder": "Digite seu Login"
            }
                                    ))
    senha = forms.CharField(label= 'Senha',
                             max_length=57, 
                             required=True,
                             widget= forms.PasswordInput(attrs={"class": "form-control",
                                                                "placeholder": "Digite sua senha"}
                                                         )
                                                         )

class CadastroForms(forms.Form):
      nome_cadastro=forms.CharField(label= 'Nome de Cadastro',
                                 max_length=50, 
                                 required=True,
                                 widget=forms.TextInput(
                                     attrs={
                                    "class": "form-control",
                                     "placeholder": "EX: João batista"
            }
                                    ))
      email= forms.CharField(label= 'Email',
                                 max_length=50, 
                                 required=True,
                                 widget=forms.EmailInput(
                                     attrs={
                                    "class": "form-control",
                                     "placeholder": "Ex: joao@teste.com.br"
            }
                                    ))
      password1 = forms.CharField(label= 'Senha',
                             max_length=57, 
                             required=True,
                             widget= forms.PasswordInput(attrs={"class": "form-control",
                                                                "placeholder": "Digite sua senha"}
                                                         )
                                                         )
    
      password2 = forms.CharField(label= 'Confirme a Senha',
                             max_length=57, 
                             required=True,
                             widget= forms.PasswordInput(attrs={"class": "form-control",
                                                                "placeholder": "Digite sua senha novamente"}
                                                         )
                                                         )
    

        
    

    
