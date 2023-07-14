from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum
from django.utils.text import slugify
from shop.models import Product, Order, OrderItem, Category
from .models import UserProfile
from django.contrib import messages
from shop.forms import ProductForm
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from decimal import Decimal
from django.contrib.admin.views.decorators import staff_member_required


class CustomLoginView(LoginView):
    template_name = 'userprofile/login.html'

    def form_valid(self, form):
        # Chama o método form_valid da classe pai para autenticar o usuário
        response = super().form_valid(form)

        # Verifica se o usuário é um administrador (superusuário)
        if self.request.user.is_superuser:
            return redirect('admin:index')  # Redireciona para a área de administração do Django
        else:
            return response  # Continua com o comportamento padrão para outros usuários


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
def my_statistics(request):
    # Filtra as compras feitas pelo usuário logado
    user_orders = Order.objects.filter(created_by=request.user)

    # Calcula o total de todas as compras
    total_purchases = user_orders.aggregate(total=Sum('total_amount'))['total']
    total_purchases = float(total_purchases) if total_purchases else 0.0

    # Calcula o valor correspondente a 23% do valor total
    tax_percentage = 0.23
    tax_amount = Decimal(total_purchases) * Decimal(tax_percentage)

    # Calcula o valor sem o imposto
    total_without_tax = total_purchases - float(tax_amount)

    # Reduz o número de casas decimais para 2
    total_purchases = round(total_purchases, 2)
    total_without_tax = round(total_without_tax, 2)
    tax_amount = round(float(tax_amount), 2)

    # Agrupa os itens das compras pelo produto e conta a quantidade comprada
    user_top_products = OrderItem.objects.filter(order__in=user_orders) \
                                          .values('product__title') \
                                          .annotate(total_quantity=Sum('quantity')) \
                                          .order_by('-total_quantity')[:5]

    # Encontra as categorias mais compradas pelo usuário
    user_top_categories = OrderItem.objects.filter(order__in=user_orders) \
                                            .values('product__category__title') \
                                            .annotate(total_quantity=Sum('quantity')) \
                                            .order_by('-total_quantity')[:5]

    context = {
        'user_top_products': user_top_products,
        'user_top_categories': user_top_categories,
        'total_purchases': total_purchases,
        'total_without_tax': total_without_tax,
        'tax_amount': tax_amount,
    }

    return render(request, 'userprofile/my_statistics.html', context)


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'userprofile/order_detail.html', {'order': order})


@login_required
def my_order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

    # Verifica se o usuário logado é o mesmo usuário associado ao pedido
    if order.created_by != request.user:
        # Caso não seja, você pode redirecionar o usuário ou exibir uma mensagem de erro
        return HttpResponse("Você não tem permissão para visualizar este pedido.")

    return render(request, 'userprofile/my_order_detail.html', {'order': order})


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
    return render(request, 'userprofile/product_form.html',
                  {'title': 'Editar Produto', 'product': product, 'form': form})


@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()
    messages.success(request, 'Produto apagado com sucesso!')
    return redirect('my_shop')


@login_required
def my_account(request):
    user_profile = request.user.userprofile
    return render(request, 'userprofile/my_account.html', {'user_profile': user_profile})


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)

            return redirect('frontpage')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'userprofile/register.html', {'user_form': user_form, 'profile_form': profile_form})


def process_statistics():
    top_products = Product.objects.annotate(total_quantity=Sum('items__quantity')).order_by('-total_quantity')[:5]

    total_quantity = Product.objects.aggregate(total_quantity=Sum('items__quantity'))['total_quantity']

    categories = Category.objects.annotate(total_quantity=Sum('products__items__quantity')).filter(total_quantity__gt=0)

    for category in categories:
        category.percentage = (category.total_quantity / total_quantity) * 100

    return top_products, categories


def process_low_stock_list():
    low_stock_products = Product.objects.filter(stock__lte=0.2 * F('initial_stock'))
    return low_stock_products


@login_required
def statistics(request):
    top_products, categories = process_statistics()
    low_stock_products = process_low_stock_list()

    context = {'top_products': top_products, 'categories': categories, 'low_stock_products': low_stock_products}
    return render(request, 'userprofile/statistics.html', context)


def get_top_buyers():
    top_buyers = UserProfile.objects.filter(is_vendor=False) \
        .annotate(total_purchases=Sum('user__orders__total_amount')) \
        .order_by('-total_purchases')[:5]

    return top_buyers


@staff_member_required
def admin_statistics(request):
    top_products, categories = process_statistics()
    order_items = OrderItem.objects.all()
    low_stock_products = process_low_stock_list()
    top_buyers = get_top_buyers()

    context = {
        'top_products': top_products,
        'categories': categories,
        'order_items': order_items,
        'low_stock_products': low_stock_products,
        'top_buyers': top_buyers,
    }
    return render(request, 'userprofile/admin_statistics.html', context)


def low_stock_list(request):
    low_stock_products = process_low_stock_list()

    return render(request, 'userprofile/low_stock_list.html', {'low_stock_products': low_stock_products})

