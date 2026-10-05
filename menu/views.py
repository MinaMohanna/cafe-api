from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Product, Table, Order, OrderItem, Catagory
from .serializers import (
    CategorySerializer, ProductSerializer, TableSerializer,
      OrderItemSerializer, OrderSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class CategoryViewSet(viewsets.ModelViewSet):
    queryset =Catagory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class ProductViewSet(viewsets.ModelViewSet):
    queryset =Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes =[AllowAny]
    filter_backends = [DjangoFilterBackend , filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category','is_available']
    search_fields = ['name','ingredients']
    ordering_fields = ['price', 'name']



class TableViewSet(viewsets.ModelViewSet):
    queryset =Table.objects.all()
    serializer_class = TableSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset =Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['table', 'status','is_paid']
    ordering_fields = ['created_at']

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer