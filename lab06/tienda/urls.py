from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:producto_id>/', views.producto, name='producto'),
    path('categoria/<str:name>/', views.products_by_category, name='products_by_category')
]