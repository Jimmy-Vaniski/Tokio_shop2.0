from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'description', 'price', 'image']
        widgets = {
            'category': forms.Select(attrs={'class': 'p-4 border-radios border-green-300'}),


        }
