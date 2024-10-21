from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

def index(request):
    return render(request, 'index.html')

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listado.html', {'productos': productos})

def registrar_producto(request):
    return render(request, 'form_registrar.html')

def insertar_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        marca = request.POST['marca']
        precio = request.POST['precio']
        Producto.objects.create(nombre=nombre, marca=marca, precio=precio)
        return redirect('listar_productos')

def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.marca = request.POST['marca']
        producto.precio = request.POST['precio']
        producto.save()
        return redirect('listar_productos')
    return render(request, 'form_actualizar.html', {'producto': producto})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listar_productos')
