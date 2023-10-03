from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *

from rest_framework import status
from rest_framework.decorators import api_view ,authentication_classes
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.settings import CONSTANTS

from .models import *

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
import django_filters

from django.db.models import Q
# Create your views here.


# product CRUD


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
def createProductView(request):
        data=request.data
        product_name = data.get("product_name", None)
        if product_name is not None:
            existing_product = Product.objects.filter(Q(product_name__iexact=product_name)).exists()
            
            if existing_product:
                return Response({'error':'Product with this same name exist'})
        
        serializer=ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def productUpdate(request, pk):
    product = Product.objects.get(id = pk)
    serializer = ProductSerializer(instance=product, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#Order CRUD

    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def createOrderView(request):
    data = request.data
    serializer = OrderSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)





@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def orderUpdateView(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(instance=order, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def CustomerCreateOrderProductView(request):
    
    product_id=request.data['product']
    quantity=int(request.data['quantity'])
    
    stock_product=Product.objects.get(id=product_id)
    Stock_serializer=ProductSerializer(stock_product)
    
    remaining_stock=int(Stock_serializer.data['stock'])
    print(remaining_stock-quantity)
    if(remaining_stock-quantity) >= 0:
        data=request.data
        serializer=orderProductSerializer(data=data,) 
        if serializer.is_valid():
            serializer.save()
            
            stock_product.stock = remaining_stock - quantity
            stock_product.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        
        return Response({'error': 'Not enough stock available'})
        

            
            
            