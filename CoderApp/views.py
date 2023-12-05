from django.shortcuts import render, redirect
import datetime
from .models import Producto
from .forms import ProductoForm
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def mostrar_fecha_actual(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'fecha_actual.html', {'fecha_actual': fecha_actual})

# def producto_list(request):
#     productos = Producto.objects.all()
#     print(productos)
#     return render(request, 'producto_list.html', {'productos': productos})

class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_list.html'
    context_object_name = 'productos'

def index(request):
    return render(request, 'index.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            return redirect('CoderApp:index')  
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form})

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'producto_form.html'
    form_class = ProductoForm
    success_url = reverse_lazy('CoderApp:producto_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto_confirm_delete.html'
    success_url = reverse_lazy('CoderApp:producto_list')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('CoderApp:index')
        else:
            # Manejo de error de inicio de sesión
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos.'})
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('CoderApp:index')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CoderApp:user_login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})