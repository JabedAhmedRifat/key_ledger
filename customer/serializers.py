from rest_framework import serializers
from .models import Customer, DebitCreditCustomer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Customer
        fields = '__all__'
        
        
class DebitCreditCustomerSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = DebitCreditCustomer
        fields = '__all__'