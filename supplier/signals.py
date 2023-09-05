from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SupplierOrder, DebitCreditSupplier

@receiver(post_save, sender=SupplierOrder)
def update_debit_credit_supplier(sender, instance, created, **kwargs):
    if created and instance.payment_due and instance.order_total > 0:
        supplier = instance.supplier
        
        supplier_entry, created = DebitCreditSupplier.objects.get_or_create(supplier=supplier)
        
        if created:
            supplier_entry.debit_balance = 0
            supplier_entry.credit_balance = instance.order_total
            supplier_entry.total_balance = instance.order_total
        else:
            supplier_entry.credit_balance += instance.order_total
            supplier_entry.total_balance += instance.order_total
        
        order_number = instance.order_number
        supplier_entry.details = f"Payment due for order {order_number}"
        supplier_entry.save()
        
        
    elif created and not instance.payment_due and instance.order_total > 0:
        supplier = instance.supplier
        supplier_entry, created = DebitCreditSupplier.objects.get_or_create(supplier=supplier)
        supplier_entry.debit_balance += instance.order_total
        supplier_entry.total_balance += instance.order_total
        supplier_entry.save()
