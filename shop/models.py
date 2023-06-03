from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    user = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/produto_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField(default=0)
    shelf = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)  # ordenar exibicao por data de criação

    def __str__(self):
        return self.title

    def get_display_price(self):
        return self.price
