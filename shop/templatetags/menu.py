"""Aqui sera onde chamarei a livraria que renderiza o meu templates."""
from django import template
from shop.models import Category

register = template.Library()


@register.inclusion_tag('core/menu.html')
def menu():
    categories = Category.objects.all()

    return {'categories': categories, }
