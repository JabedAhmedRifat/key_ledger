from django.contrib import admin
from .models import Supplier , SupplierOrder , SupplierOrderProduct ,DebitCreditSupplier
# Register your models here.
admin.site.register(Supplier)
admin.site.register(SupplierOrder)
admin.site.register(SupplierOrderProduct)
admin.site.register(DebitCreditSupplier)