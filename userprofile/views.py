from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from .models import UserProfile
from shop.forms import ProductForm
from shop.models import Product, Category


def vendor_details(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, 'userprofile/vendor_details.html', {'user': user})

@login_required
def my_shop(request):
    return render(request, 'userprofile/my_shop.html')


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
            return redirect('my_shop')
    else:
        form = ProductForm()
    return render(request, 'userprofile/add_product.html', {'title': 'Editar Produto', 'form': form})


@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    form = ProductForm()
    return render(request, 'userprofile/add_product.html', {'title': 'Editar Produto', 'form': form})


@login_required
def my_account(request):
    return render(request, 'userprofile/my_account.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            userprofile = UserProfile.objects.create(user=user)

            return redirect('frontpage')

    else:
        form = UserCreationForm()
    return render(request, 'userprofile/register.html', {'form': form})
