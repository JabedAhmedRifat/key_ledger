from rest_framework import serializers
from .models import *
from num2words import num2words


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        

# class SupplierOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SupplierOrder
#         fields = "__all__"
        
class SupplierOrderSerializer(serializers.ModelSerializer):
    
    order_total_words = serializers.SerializerMethodField()
    
    class Meta:
        model = SupplierOrder
        fields = '__all__'
        read_only_fields = ('order_number',)

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.order_number = f'DSA{instance.id}'
        instance.save()
        return instance
    
    
    def get_order_total_words(self,data):
        order_total = data.order_total
        if order_total is not None:
            return num2words(order_total, to='cardinal')
        else: 
            return ""
    
    
    
        
class SupplierOrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierOrderProduct
        fields = "__all__"
        
        
class DebitCreditSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebitCreditSupplier
        fields = "__all__"