from django.contrib import admin
from .models import Catagory, Product, Table, Order,OrderItem
# Register your models here.

admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(OrderItem)