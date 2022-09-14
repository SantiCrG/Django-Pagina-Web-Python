"""SOFTWAT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.paginaprincipal, name='index'),
    path('clienteinicio/', views.ClienteInicio, name='iniciocliente'),
    path('mision/', views.Mision, name='mision'),
    path('catpinturas/', views.CatPinturas, name='catpinturas'),
    path('catrollos/', views.CatRollos, name='catrollos'),
    path('aplicacion/', views.Aplicacion, name='aplicacion'),
    path('domicilio/', views.Domicilio, name='domicilio'),
    path('carrito/', views.Carrito, name='carrito'),
    path('login/', views.login_view, name='login'),
    path('PQRS/', views.PQRS, name='PQRS'),
]
