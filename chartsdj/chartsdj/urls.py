# -*- coding: utf-8 -*-
"""chartsdj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#import apps views
from graficas.views import grafica_simple, example_simple_db, notas_por_estado


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^grafica_simple$', grafica_simple, name='grafica_simple'),
    url(r'^example_db$', example_simple_db, name='example_simple_db'),
    url(r'^$', notas_por_estado, name='notas_por_estado')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
