from rest_framework import viewsets
from .models import Product, Table, Order, OrderItem, Catagory
from .serializers import (
    CategorySerializer, ProductSerializer, TableSerializer,
      OrderItemSerializer, OrderSerializer,
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset =Catagory.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset =Product.objects.all()
    serializer_class = ProductSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset =Table.objects.all()
    serializer_class = TableSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset =Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer