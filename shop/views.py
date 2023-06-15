from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Order, OrderItem
from django.db.models import Q
from .cart import Cart
from .forms import OrderForm


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add_item(product_id)  # ATENTION

    return redirect('cart_view')


@login_required
def check_to_buy(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            total_price = 0
            for item in cart:
                product = item['product']
                total_price += product.price * int(item['quantity'])

            order = form.save(commit=False)
            order.created_by = request.user
            order.total_amount = total_price
            order.save()

            for item in cart:
                product = item['product']
                quantity = int(item['quantity'])
                price = product.price * quantity

                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)
                cart.clear()

                return redirect('my_account')
    else:
        form = OrderForm()
    return render(request, 'shop/check_to_buy.html', {'cart': cart, 'form': form})


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
    cart.remove_item(product_id)  # ATENTION

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
