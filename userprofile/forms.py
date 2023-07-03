from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    nome = forms.CharField(
        label='Nome',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite seu nome',
        })
    )

    apelido = forms.CharField(
        label='Apelido',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite seu apelido',
        })
    )

    Nif = forms.CharField(
        label='NIF',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite seu NIF',
        })
    )

    endereco = forms.CharField(
        label='Endereço',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite seu endereço',
        })
    )

    cep = forms.CharField(
        label='CEP',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite seu CEP',
        })
    )

    telefone = forms.CharField(
        label='Telefone',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite seu telefone',
        })
    )

    is_vendor = forms.BooleanField(
        label='Is Vendor',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'w-full p-4 border border-green-600',
        })
    )

    nome_empresa = forms.CharField(
        label='Nome da Empresa',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite o nome da empresa',
        })
    )

    nif_empresa = forms.CharField(
        label='NIF da Empresa',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite o NIF da empresa',
        })
    )

    endereco_empresa = forms.CharField(
        label='Endereço da Empresa',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite o endereço da empresa',
        })
    )

    cep_empresa = forms.CharField(
        label='CEP da Empresa',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite o CEP da empresa',
        })
    )

    telefone_empresa = forms.CharField(
        label='Telefone da Empresa',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite o telefone da empresa',
        })
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite seu email',
        })
    )

    email_empresa = forms.EmailField(
        label='Email da Empresa',
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite o email da empresa',
        })
    )

    class Meta:
        model = UserProfile
        fields = [
            'email',
            'nome',
            'apelido',
            'Nif',
            'endereco',
            'cep',
            'telefone',
            'is_vendor',
            'nome_empresa',
            'nif_empresa',
            'endereco_empresa',
            'cep_empresa',
            'telefone_empresa',

            'email_empresa',
        ]
