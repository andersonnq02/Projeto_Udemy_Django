from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# Gambiarra para ver as imagens no navegador
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('empresa/', include('apps.empresas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('documento/', include('apps.documentos.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# GAmbiarra apra ver arquivos staticos, porém recomendado pela própria documentação do django
