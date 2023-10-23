from django.urls import path
from . import views

urlpatterns = [
    path('fecha-actual/', views.mostrar_fecha_actual, name='mostrar_fecha_actual'),
    path('productos/', views.producto_list, name='producto_list'),
    path('index/', views.index, name='index'),
]
