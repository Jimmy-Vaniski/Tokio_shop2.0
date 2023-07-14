from django.contrib import admin

from .models import Category, Product, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    list_filter = ('title',)
    list_display_links = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'stock', 'initial_stock', 'shelf', 'status')
    list_filter = ('category', 'status')
    list_display_links = ('title', 'category',)
    list_editable = ('price', 'shelf', )
    search_fields = ('title', 'category', 'price', 'stock', 'initial_stock', 'shelf', 'status')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'total_amount', 'city', 'county', 'created_at', 'shipping_address')
    search_fields = ('id', 'first_name', 'total_amount', 'city', 'county', 'created_at', 'shipping_address')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order')
    list_filter = ('id', 'order')
    list_display_links = ('id', 'order')
    search_fields = ('id', 'order', )

