"""
URL configuration for meuprojeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('episodios/<str:nome_serie>/', views.episodios, name="episodios_series"),
    path('filmes/', views.filmes, name="filmes"),
    path('series/', views.series, name="series"),
    path('serie/<str:nome_serie>/<str:nome_episodio>/', views.transmitir_serie, name="transmite_serie"),
    path('filme/<str:nome_pasta>/<str:nome_filme>/', views.transmitir_filme, name="transmite_filme")
]
