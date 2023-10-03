from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *


from rest_framework.decorators import api_view ,authentication_classes, permission_classes 
from knox.auth import TokenAuthentication


from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import *


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def createCustomerView(request):
    data = request.data
    customer_shop_name = data.get("customer_shop_name", None)
    if customer_shop_name is not None:
        existing_customer = Customer.objects.filter(customer_shop_name__iexact=customer_shop_name).exists()
        
        if existing_customer:
            return Response({"error":"Customer with this same name exist"})
           
    serializer = CustomerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)




@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def customerUpdate(request, pk):
    customer = Customer.objects.get(id = pk)
    serializer = CustomerSerializer(instance=customer, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




# Debit Credit Information of Customer




@api_view(['POST'])
def createCustomerDebitCredit(request):
    data = request.data 
    serializer = DebitCreditCustomerSerilaizer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)



@api_view(['POST'])
def customerDebitCreditUpdate(request,pk):
    debit_credit = DebitCreditCustomer.objects.get(id=pk)
    serializer = DebitCreditCustomerSerilaizer(instance = debit_credit, data= request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)