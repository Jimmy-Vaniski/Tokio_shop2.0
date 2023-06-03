from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'shop/category_details.html', {'category': category, 'products': products})

 
def product_detail(request, category_slug,  slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})
