from django.shortcuts import render, redirect
import datetime
from .models import Producto
from .forms import ProductoForm
# Create your views here.

def mostrar_fecha_actual(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'fecha_actual.html', {'fecha_actual': fecha_actual})

def producto_list(request):
    productos = Producto.objects.all()
    print(productos)
    return render(request, 'producto_list.html', {'productos': productos})

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