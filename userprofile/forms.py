from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-4 border border-green-600 rounded-md h-8',
            'placeholder': 'Digite sua senha',
        })
    )

    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-4 border border-green-600 rounded-md h-8',
            'placeholder': 'Confirme sua senha',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-green-600 rounded-md h-8',
                'placeholder': 'Digite seu nome de usuário',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-4 border border-green-600 rounded-md h-8',
                'placeholder': 'Digite seu email',
            }),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'nome', 'apelido', 'Nif', 'endereco', 'cep', 'telefone', 'is_vendor',
            'nome_empresa', 'nif_empresa', 'endereco_empresa', 'cep_empresa',
            'telefone_empresa', 'email_empresa'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-green-600 rounded-md h-8',
                'placeholder': 'Digite seu nome',
            }),
            'apelido': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-green-600 rounded-md h-8',
                'placeholder': 'Digite seu apelido',
            }),
            'Nif': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-green-600 rounded-md h-8',
                'placeholder': 'Digite seu NIF',
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-green-600 rounded-md h-8',
                'placeholder': 'Digite seu endereço',
            }),
            'cep': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-green-600 rounded-md h-8',
                'placeholder': 'Digite seu CEP',
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-green-600 rounded-md h-8',
                'placeholder': 'Digite seu telefone',
            }),
            'is_vendor': forms.CheckboxInput(attrs={
                'class': '',
            }),
            'nome_empresa': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-green-600 rounded-md h-8',
                'placeholder': 'Digite o nome da empresa',
            }),
            'nif_empresa': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-green-600 rounded-md h-8',
                'placeholder': 'Digite o NIF da empresa',
            }),
            'endereco_empresa': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-green-600 rounded-md h-8',
                'placeholder': 'Digite o endereço da empresa',
            }),
            'cep_empresa': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-green-600 rounded-md h-8',
                'placeholder': 'Digite o CEP da empresa',
            }),
            'telefone_empresa': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-green-600 rounded-md h-8',
                'placeholder': 'Digite o telefone da empresa',
            }),
            'email_empresa': forms.EmailInput(attrs={
                'class': 'w-full p-4 border border-green-600 rounded-md h-8',
                'placeholder': 'Digite o email da empresa',
            }),
        }
