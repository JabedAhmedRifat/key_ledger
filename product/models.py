from django.db import models
from supplier.models import Supplier
from customer.models import Customer

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField(max_length=500, blank=True)
    selling_price = models.IntegerField(blank=True)
    buying_price = models.IntegerField(blank=True)
    supplier = models.ForeignKey('supplier.Supplier', on_delete=models.CASCADE,related_name='supplierProduct')
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.product_name
    
    
# invoice use as Order    

# Customer Order model

class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted','Accepted'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'), 
    )
    
    order_number = models.CharField(max_length=30)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50, blank=True,null=True)
    order_note = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=10 , choices=STATUS, default='New')
    payment_due = models.BooleanField(default=True)
    order_total = models.FloatField()
    invoice_date = models.DateTimeField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = f'CUS{self.id}'
        super().save(*args, **kwargs)
    

# customer OrderProduct Model    

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    orederd = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)