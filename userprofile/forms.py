from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nome', 'apelido', 'Nif', 'endereco', 'cep', 'telefone', 'is_vendor', 'nome_empresa', 'nif_empresa',
                  'endereco_empresa', 'cep_empresa', 'telefone_empresa', 'email_empresa']
