from rest_framework import serializers
from.models import Catagory, Product, Order, Table, OrderItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)


    class Meta:
        model = Order
        fields = ['id', 'table', 'created_at', 'status', 'is_paid', 'items']

    def create(self, validated_data):
        items_data= validated_data.pop('items')

        order= Order.objects.create(**validated_data)


        for item_data in items_data:
            OrderItem.objects.create(order= order , **item_data)

        return order
    