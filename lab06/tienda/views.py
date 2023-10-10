from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias  = Categoria.objects.order_by('nombre')
    context = {'product_list': product_list, 'categorias': categorias}
    return render(request,'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias  = Categoria.objects.order_by('nombre')
    context = {'producto' : producto, 'categorias': categorias}
    return render(request,'producto.html', context)

def products_by_category(request, name):
    categoria = Categoria.objects.get(nombre = name)
    products_by_category = categoria.producto_set.all()
    categorias  = Categoria.objects.order_by('nombre')
    context = {'products_by_category' : products_by_category , 'categorias': categorias}
    return render (request,'categoria.html', context)