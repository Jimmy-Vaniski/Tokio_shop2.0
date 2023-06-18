from django.urls import path
from . import views


urlpatterns = [

    path('search/', views.search, name='search'),

    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('remove_from_cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('change_quantity/<str:product_id>/', views.change_quantity, name='change_quantity'),

    path('cart/', views.cart_view, name='cart_view'),

    path('cart/check_to_buy/', views.check_to_buy, name='check_to_buy'),

    path('cart/success/', views.success, name='success'),

    path('<slug:slug>/', views.category_details, name='category_details'),

    path('<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail'),



]















