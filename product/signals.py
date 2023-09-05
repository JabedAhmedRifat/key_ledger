from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from customer.models import DebitCreditCustomer

@receiver(post_save, sender=Order)
def update_debit_credit_supplier(sender, instance, created, **kwargs):
    if created and instance.payment_due and instance.order_total > 0:
        customer = instance.customer
        
        customer_entry, created = DebitCreditCustomer.objects.get_or_create(customer=customer)
        
        if created:
            customer_entry.credit_balance = 0
            customer_entry.debit_balance = instance.order_total
            customer_entry.total_balance = instance.order_total
        else:
            customer_entry.debit_balance += instance.order_total
            customer_entry.total_balance += instance.order_total
        
        instance.refresh_from_db() 
        order_number = instance.order_number
        customer_entry.details = f"Payment due for order {order_number}"
        customer_entry.save()
        
    elif created and not instance.payment_due and instance.order_total > 0:
        customer = instance.customer
        customer_entry, created = DebitCreditCustomer.objects.get_or_create(customer=customer)
        customer_entry.credit_balance += instance.order_total
        customer_entry.total_balance += instance.order_total
        customer_entry.save()
        
