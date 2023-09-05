from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        
# customer Order an and Order product Serializer
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('order_number',)

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.order_number = f'CUS{instance.id}'
        instance.save()
        return instance
    
        
class orderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'