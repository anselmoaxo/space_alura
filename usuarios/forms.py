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

    
