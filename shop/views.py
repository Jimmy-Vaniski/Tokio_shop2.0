from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.db.models import Q
from .cart import Cart


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add_item(product_id)  # ATENTION

    return redirect('cart_view')


def change_quantity(request, product_id):
    action = request.GET.get('action', '')
    if action:
        quantity = 1
        if action == 'decrease':
            quantity = -1
        cart = Cart(request)
        cart.add_item(product_id, quantity, True)

    return redirect('cart_view')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove_item(product_id) # ATENTION

    return redirect('cart_view')


def cart_view(request):
    cart_ = Cart(request)

    return render(request, 'shop/cart_view.html', {'cart': cart_})


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(status=Product.ACTIVATED).filter(
        Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'shop/search.html', {'query': query, 'products': products})


def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ACTIVATED)
    return render(request, 'shop/category_details.html', {'category': category, 'products': products})


def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVATED)
    return render(request, 'shop/product_detail.html', {'product': product})
