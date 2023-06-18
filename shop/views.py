from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Order, OrderItem
from django.db.models import Q
from .cart import Cart
from .forms import OrderForm
from django.conf import settings
import json
import stripe
from django.http import JsonResponse


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add_item(product_id)  # ATENTION

    return redirect('cart_view')


def success(request):
    return render(request, 'shop/success.html')


@login_required
def check_to_buy(request):
    cart = Cart(request)
    if cart.get_total_values == 0:
        return redirect('cart_view')
    if request.method == 'POST':
        data = json.loads(request.body)

        first_name = data['first_name'],
        last_name = data['last_name'],
        shipping_address = data['shipping_address'],
        postal_code = data['postal_code'],
        city = data['city'],
        county = data['county'],

        if first_name and last_name and shipping_address and postal_code and city and county:

            form = OrderForm(request.POST)

            total_price = 0
            items = []
            for item in cart:
                product = item['product']
                total_price += product.price * int(item['quantity'])
                items.append({
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': product.title,

                        },
                        'unit_amount': int(product.price)
                    },
                        'quantity': item['quantity']

                })

            stripe.api_key = settings.STRIPE_SECRET_KEY
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=items,
                mode='payment',
                success_url='http://127.0.0.1:8000/cart/success',
                cancel_url='http://127.0.0.1:8000/cart/',

            )
            payment_intent = session.payment_intent

            order = Order.objects.create(
                first_name=first_name,
                last_name=last_name,
                shipping_address=shipping_address,
                postal_code=postal_code,
                city=city,
                county=county,

                created_by=request.user,
                is_paid=True,
                payment_intent=str(payment_intent),
                total_amount=total_price,

            )

            for item in cart:
                product = item['product']
                quantity = int(item['quantity'])
                price = product.price * quantity

                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)
                cart.clear()

                return JsonResponse({'session': session, 'order': payment_intent})
    else:
        form = OrderForm()
    return render(request, 'shop/check_to_buy.html', {'cart': cart, 'form': form, 'pub_key': settings.STRIPE_PUB_KEY,})


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
