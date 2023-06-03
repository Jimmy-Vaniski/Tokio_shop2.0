from django.contrib import admin
from django.urls import path
from core.views import frontpage, about


urlpatterns = [

    path('', frontpage, name='frontpage'),
    path('about', about, name='about'),
    path('admin/', admin.site.urls),
]
