from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_shop_name = models.CharField(max_length=255)
    customer_shop_address = models.TextField()
    contact_person_name = models.CharField(max_length=255)
    contact_person_phone = models.CharField(max_length=50)
    
    def __str__(self):
        return self.customer_shop_name
    
class DebitCreditCustomer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    debit_balance= models.FloatField(default=0)
    credit_balance= models.FloatField(default=0)
    total_balance = models.FloatField(default=0)
    details= models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
 