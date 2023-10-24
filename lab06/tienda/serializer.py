from rest_framework import serializers
from .models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Categoria
        fields = ('id','nombre', 'pub_date')


class ProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Producto
        fields = ('id','categoria','nombre', 'precio', 'stock', 'pub_date')