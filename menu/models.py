from django.db import models

# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "دسته بندی ها"


class Product(models.Model):
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.TextField(blank=True, null=True, help_text='محتویات محصول')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

class Table(models.Model):
    number = models.IntegerField(unique=True)
    is_accupied = models.BooleanField(default=False)


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار'),
        ('preparing', 'در حال  آماده سازی'),
        ('served', 'سرو شده'),
        ('paid', 'پرداخت شده'),
    ]
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    status =models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_paid = models.BooleanField(default=False)
    def __str__(self):
        return f"سفارش میز {self.table.number} - {self.created_at}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
