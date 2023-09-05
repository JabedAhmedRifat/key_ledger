from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *


from rest_framework.decorators import api_view ,authentication_classes, permission_classes 
from knox.auth import TokenAuthentication

from .pagination import StandardPagination


from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def allCustomerView(request):
    if request.method == "GET":
        data = Customer.objects.all().order_by('-id')
        paginator = StandardPagination()
        result_page = paginator.paginate_queryset(data, request)
        serializer = CustomerSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def customerDetail(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)





@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def customerDelete(request, pk):
    customer = Customer.objects.get(id = pk )
    customer.delete()
    return Response({
        "message" : "Customer delete successfully"
    })






#Searching customer filtering

    
class searchCustomer(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer_shop_name']
    pagination_class = StandardPagination
    




# Debit Credit Information of Customer

@api_view(['GET'])
def customerAllDebitCreditInfo(request):
    if request.method == 'GET':
        data = DebitCreditCustomer.objects.all().order_by('-id')
        paginator = StandardPagination()
        result_page = paginator.paginate_queryset(data, request)
        serializer = DebitCreditCustomerSerilaizer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)




@api_view(['GET'])
def customerDebitCreditDetail(request,pk):
    debit_credit = DebitCreditCustomer(id=pk)
    serializer = DebitCreditCustomerSerilaizer(debit_credit)
    return Response(serializer.data)





@api_view(['DELETE'])
def customerDebitCreditDelete(request,pk):
    debit_credit = DebitCreditCustomer(id = pk)
    debit_credit.delete()
    return Response ({"message":"Customer Debit Credit DELETED successfully"})

    