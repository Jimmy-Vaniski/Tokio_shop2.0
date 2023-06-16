from django.shortcuts import render
from shop.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def frontpage(request):
    product_list = Product.objects.filter(status=Product.ACTIVATED)
    paginator = Paginator(product_list, 5)  # Exibe 6 produtos por página

    page = request.GET.get('page')
    try:
        products = paginator.get_page(page)
    except PageNotAnInteger:
        products = paginator.get_page(1)
    except EmptyPage:
        products = paginator.get_page(paginator.num_pages)

    return render(request, 'core/frontpage.html', {'products': products})



def about(request):
    return render(request, 'core/about.html')
