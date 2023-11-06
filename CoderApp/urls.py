from django.urls import path
from . import views


app_name = 'CoderApp'


urlpatterns = [
    path('fecha-actual/', views.mostrar_fecha_actual, name='mostrar_fecha_actual'),
    path('productos/', views.ProductoListView.as_view(), name='producto_list'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/editar/<int:pk>/', views.ProductoUpdateView.as_view(), name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.ProductoDeleteView.as_view(), name='eliminar_producto'),
    path('index/', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='user_register'),
]

