from rest_framework import serializers
from .models import *

from num2words import num2words

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        
# customer Order an and Order product Serializer
    
class OrderSerializer(serializers.ModelSerializer):
    order_total_word = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('order_number',)

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.order_number = f'CUS{instance.id}'
        instance.save()
        return instance
    
    def get_order_total_word(self, data):
        order_total = data.order_total
        if order_total is not None:
            return num2words(order_total)
        else:
            return ""
    
        
class orderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = '__all__'