from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import low_stock_list, statistics, CustomLoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('my_account/', views.my_account, name='my_account'),
    path('my_account/my_order_detail/<int:pk>/', views.my_order_detail, name='my_order_detail'),
    path('my_shop/', views.my_shop, name='my_shop'),

    path('my_shop/order_detail/<int:pk>/', views.order_detail, name='order_detail'),

    path('my_shop/add-product/', views.add_product, name='add_product'),
    path('my_shop/edit-product/<int:pk>/', views.edit_product, name='edit_product'),
    path('my_shop/delete-product/<int:pk>/', views.delete_product, name='delete_product'),
    path('low_stock_list/', low_stock_list, name='low_stock_list'),
    path('statistics/', statistics, name='statistics'),
    path('vendors/<int:pk>/', views.vendor_details, name='vendor_details'),

]

