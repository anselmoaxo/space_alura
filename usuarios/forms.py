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
                                                         ))
      
      # valida se Nome Cadastro contém espaços                                               
      def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("*Espaços não são permitidos no campo Nome de Cadastro")
            else:
                return nome
            
       # valida senha são iguais para o cadastro     
      def clean_password2(self):
        senha1 = self.cleaned_data.get("password1")
        senha2 = self.cleaned_data.get("password2")
        if senha1 and senha2:
            
            if senha1 != senha2:
                raise forms.ValidationError("*Erro , Senhas não coincidem")
            else:
                return senha2
    

            

            
            
     