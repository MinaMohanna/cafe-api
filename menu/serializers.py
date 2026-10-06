from rest_framework import serializers
from.models import Catagory, Product, Order, Table, OrderItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields =['image']

    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolut_url(obj.image.url)
            return obj.image.url
        return None


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
    