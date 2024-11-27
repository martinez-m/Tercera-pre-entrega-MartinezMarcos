from django.shortcuts import render, redirect
from .forms import ProductoForm, ClienteForm, PedidoForm
from .models import Producto, Cliente, Pedido

def inicio(request):
    return render(request, 'tienda/base.html')

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductoForm()
    return render(request, 'tienda/crear_producto.html', {'form': form})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()
    return render(request, 'tienda/crear_cliente.html', {'form': form})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PedidoForm()
    return render(request, 'tienda/crear_pedido.html', {'form': form})

def buscar_producto(request):
    query = request.GET.get('q') 
    resultados = Producto.objects.filter(nombre__icontains=query) if query else []
    return render(request, 'tienda/buscar_producto.html', {'resultados': resultados, 'query': query})
