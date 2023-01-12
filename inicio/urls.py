#from django.contrib import admin
from django.urls import path
from inicio import views
from .views import *


urlpatterns = [
    
    path('', views.pre, name='Hola'),
    path('s', views.Bienvenida, name='Bienvenida'),
    path('<int:product_id>', views.linkjc, name='linkjc'),
    path('<int:product_id>/', views.detalle, name='detalle'),
    path('gracias', views.gracias, name='gracias'),
    path('Categorias', views.Cate, name='Categorias'),
    path('cat/<int:category_id>/', views.filtrojc, name='filtro'),
    
]
