from rest_framework import serializers
from .models import *

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        

# class SupplierOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SupplierOrder
#         fields = "__all__"
        
class SupplierOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierOrder
        fields = '__all__'
        read_only_fields = ('order_number',)

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.order_number = f'DSA{instance.id}'
        instance.save()
        return instance
    
    
    
        
class SupplierOrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierOrderProduct
        fields = "__all__"
        
        
class DebitCreditSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebitCreditSupplier
        fields = "__all__"