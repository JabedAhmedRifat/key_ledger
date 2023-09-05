from django.db import models
# from product.models import Product
# from django.apps import apps


# Create your models here.

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=255)
    supplier_address = models.TextField()
    contact_person_name = models.CharField(max_length=255)
    contact_person_phone = models.CharField(max_length=50)
    
    def __str__(self):
        return self.supplier_name
    
    
class SupplierOrder(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted','Accepted'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'), 
    )
    
    order_number = models.CharField(max_length=30)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50, blank=True,null=True)
    order_note = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=10 , choices=STATUS, default='New')
    payment_due = models.BooleanField(default=True)
    order_total = models.FloatField(null=True)
    invoice_date = models.DateTimeField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = f'DSA{self.id}'
        super().save(*args, **kwargs)

    
class SupplierOrderProduct(models.Model):
    order = models.ForeignKey(SupplierOrder, on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class DebitCreditSupplier(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    debit_balance= models.IntegerField(default=0)
    credit_balance= models.IntegerField(default=0)
    total_balance = models.IntegerField(default=0)
    details= models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
