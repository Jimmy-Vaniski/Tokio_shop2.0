from django.shortcuts import render
from shop.models import Product


def frontpage(request):
    products = Product.objects.filter(status=Product.ACTIVATED)[0:6]
    return render(request, 'core/frontpage.html', {'products': products})


def about(request):
    return render(request, 'core/about.html')
