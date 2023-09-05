from django.contrib import admin
from .models import Customer , DebitCreditCustomer
# Register your models here.

admin.site.register(Customer)
admin.site.register(DebitCreditCustomer)