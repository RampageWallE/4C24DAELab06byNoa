from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Producto, Categoria
from .serializer import CategoriaSerializer, ProductoSerializer

from django.shortcuts import render, get_object_or_404

class indexView(APIView):
    template_name = 'index.html'
    def get(self, request):
        product_list = Producto.objects.order_by('nombre')
        categorias  = Categoria.objects.order_by('nombre')
        serProductos = ProductoSerializer(product_list, many=True).data
        serCategorias = CategoriaSerializer(categorias, many=True).data
        context = {'product_list': serProductos, 'categorias': serCategorias}
        # return Response(data=context,status=status.HTTP_200_OK, template_name='index.html')
        return render(request, 'index.html', context)
    
class productoView(APIView):
    def get(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        categorias  = Categoria.objects.order_by('nombre')
        serProductos = ProductoSerializer(producto, many=False).data
        serCategorias = CategoriaSerializer(categorias, many=True).data
        context = {'producto' : serProductos, 'categorias': serCategorias}
        # return render(request,'producto.html', context)
        return render(request,'producto.html', context)


class Products_by_categoryView(APIView):
    def get(self, request, name):
        categoria = Categoria.objects.get(nombre = name)
        products_by_category = categoria.producto_set.all()
        categorias  = Categoria.objects.order_by('nombre')
        serProductos = ProductoSerializer(products_by_category, many=True).data
        serCategorias = CategoriaSerializer(categorias, many=True).data
        context = {'products_by_category' : serProductos , 'categorias': serCategorias}
        return render (request,'categoria.html', context)