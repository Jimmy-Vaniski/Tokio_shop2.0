from django import forms
from .models import Product, Order
from django.utils.text import slugify


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'shipping_address', 'postal_code', 'city', 'county',  'goods' )


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
