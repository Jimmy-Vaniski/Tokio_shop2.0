from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from shop.models import Product, Order, OrderItem, Category
from .models import UserProfile
from django.contrib import messages
from shop.forms import ProductForm
from django.shortcuts import get_object_or_404
from .forms import UserProfileForm


def vendor_details(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Product.ACTIVATED)
    return render(request, 'userprofile/vendor_details.html', {'user': user, 'products': products})


@login_required
def my_shop(request):
    products = request.user.products.exclude(status=Product.DELETED)
    order_items = OrderItem.objects.filter(product__user=request.user)
    return render(request, 'userprofile/my_shop.html', {'products': products, 'order_items': order_items})


@login_required
def statistics(request):
    top_products = Product.objects.annotate(total_quantity=Sum('items__quantity')).order_by('-total_quantity')[:5]

    # Obter a quantidade total vendida de todos os produtos
    total_quantity = Product.objects.aggregate(total_quantity=Sum('items__quantity'))['total_quantity']

    # Obter a contagem de vendas por categoria
    categories = Category.objects.annotate(total_quantity=Sum('products__items__quantity')).filter(total_quantity__gt=0)

    # Calcular a porcentagem de vendas para cada categoria
    for category in categories:
        category.percentage = (category.total_quantity / total_quantity) * 100

    context = {'top_products': top_products, 'categories': categories}
    return render(request, 'userprofile/statistics.html', context)


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'userprofile/order_detail.html', {'order': order})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()
            messages.success(request, 'Produto adicionado com sucesso!')
            return redirect('my_shop')
    else:
        form = ProductForm()
    return render(request, 'userprofile/product_form.html', {'title': 'Adicionar Produto', 'form': form})


def low_stock_list(request):
    low_stock_products = Product.objects.filter(stock__lte=0.2 * F('initial_stock'))
    # teste para retornar no terminal se tenho retorno correto da função
    '''for product in low_stock_products: 
        print("Título: ", product.title)
        print("Estoque: ", product.stock)
        print("Estoque Inicial: ", product.initial_stock)
        print("-------------------------")'''

    return render(request, 'userprofile/low_stock_list.html', {'low_stock_products': low_stock_products})


@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto editado com sucesso!')
            return redirect('my_shop')
    else:
        form = ProductForm(instance=product)
    return render(request, 'userprofile/product_form.html', {'title': 'Editar Produto', 'product': product, 'form': form})


@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()
    messages.success(request, 'Produto apagado com sucesso!')
    return redirect('my_shop')


@login_required
def my_account(request):

    return render(request, 'userprofile/my_account.html')


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('frontpage')

    else:
        user_form = UserCreationForm()
        profile_form = UserProfileForm()

    return render(request, 'userprofile/register.html', {'user_form': user_form, 'profile_form': profile_form})
