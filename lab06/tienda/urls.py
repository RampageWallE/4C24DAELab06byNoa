from django.urls import path

from . import views

urlpatterns = [
    path('',views.indexView.as_view(), name='index'),
    path('producto/<int:producto_id>/', views.productoView.as_view(), name='producto'),
    path('categoria/<str:name>/', views.Products_by_categoryView.as_view(), name='products_by_category')
]