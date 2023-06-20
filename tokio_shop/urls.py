from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import frontpage, about
from django.views.generic import TemplateView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='core/about.html'), name='about'),

    path('admin/', admin.site.urls),

    path('', include('userprofile.urls')),
    path('', include('shop.urls')),
    path('', frontpage, name='frontpage'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# concatenar para extender url às imagens
