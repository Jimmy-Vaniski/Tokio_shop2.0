from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nome', 'Nif', 'is_vendor', 'nome_empresa', 'nif_empresa', 'email_empresa')
    list_filter = ('is_vendor',)
    list_display_links = ('user', 'nome', 'Nif', 'is_vendor', 'nome_empresa', 'nif_empresa', 'email_empresa')
    search_fields = ('user', 'nome', 'nome_empresa', 'nif_empresa', 'email_empresa')


