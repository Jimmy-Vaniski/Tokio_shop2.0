from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from io import BytesIO
from PIL import Image


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    SKETCH = 'rascunho'
    WAITING_APPROVAL = 'aguardando aprovação'
    ACTIVATED = 'ativado'
    DELETED = 'apagado'
    STATUS_CHOICES = (
        (SKETCH, 'Rascunho'),
        (WAITING_APPROVAL, 'Aguardando aprovação'),
        (ACTIVATED, 'Ativado'),
        (DELETED, 'Apagado'),
    )
    user = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/produto_images/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/produto_images/thumbnail/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField(default=0)
    shelf = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVATED)

    class Meta:
        ordering = ('-created_at',)  # ordenar exibicao por data de criação

    def __str__(self):
        return self.title

    def get_display_price(self):
        return self.price

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.create_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'media/suport/PRODUTO-SEM-IMAGEM.jpg'

    def create_thumbnail(self, image, size=(200, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, format='JPEG', quality=85)
        name = image.name.replace('uploads/produto_images/', '')
        thumbnail = File(thumb_io, name=name)

        return thumbnail
