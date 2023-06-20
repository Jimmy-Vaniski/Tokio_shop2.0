from django import forms
from .models import Product, Order
from django.utils.text import slugify


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nome',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite seu nome',
        })
    )
    last_name = forms.CharField(
        label='Sobrenome',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite seu sobrenome',
        })
    )
    shipping_address = forms.CharField(
        label='Endereço de Envio',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite seu endereço de envio',
        })
    )
    postal_code = forms.CharField(
        label='CEP',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite seu CEP',
        })
    )
    city = forms.CharField(
        label='Cidade',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite sua cidade',
        })
    )
    county = forms.CharField(
        label='Estado',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite seu estado',
        })
    )

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'shipping_address', 'postal_code', 'city', 'county')



class ProductForm(forms.ModelForm):
    price = forms.DecimalField(
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite o preço do produto',
        })
    )
    stock = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': 'w-full p-4 border border-green-600',
            'placeholder': 'Digite a quantidade em estoque',
        })
    )

    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image', 'stock', 'shelf')
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full p-4 border border-green-600',
                'placeholder': 'Selecione a categoria',
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-green-600',
                'placeholder': 'Digite o título do produto',
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-4 border border-green-600',
                'placeholder': 'Digite a descrição do produto',
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full p-4 border border-green-600',
            }),
            'shelf': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-green-600',
                'placeholder': 'Digite o local de armazenamento',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title:
            cleaned_data['slug'] = slugify(title)
        return cleaned_data
