from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view , authentication_classes
from knox.auth import TokenAuthentication

from rest_framework.filters import SearchFilter

from customer.pagination import StandardPagination

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from product.models import *
from product.models import Product

from .filters import SupplierOrderFilter 

# from .filters import filter_orders_weekly, filter_orders_monthly, filter_orders_yearly

from product.serializers import ProductSerializer
# Create your views here.


# supplier CRUD

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def allSupplierView(request):
    if request.method=="GET":
        data=Supplier.objects.all().order_by('-id')
        paginator = StandardPagination()
        result_page = paginator.paginate_queryset(data, request)
        serializer=SupplierSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def supplierDetail(request,pk):
    supplier = Supplier.objects.get(id = pk)
    serializer = SupplierSerializer(supplier)
    return Response(serializer.data)
    


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def supplierDelete(request, pk):
    supplier = Supplier.objects.get(id = pk)
    supplier.delete()
    return Response({
        "message" : "Supplier delete successfully"
    })



# supplier order CRUD

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def allSupplierOrderView(request):
    if request.method == 'GET':
        data = SupplierOrder.objects.all().order_by('-id')
        paginator = StandardPagination()
        result_page = paginator.paginate_queryset(data, request)
        serializer = SupplierOrderSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def supplierOrderDetailView(request, pk):
    supplierOrder = SupplierOrder.objects.get(id=pk)
    serializer = SupplierOrderSerializer(supplierOrder)
    return Response(serializer.data)
    


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def supplierOrderDeleteView(request, pk):
    supplierOrder = SupplierOrder.objects.get(id=pk)
    supplierOrder.delete()
    return Response({
        "message" : "Supplier Order Delete Successfully"
    })



# supplier Order Product Stock change

# filter by order 

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def supplierProductInOrderView(request, supplierOrder_id):
    supplierOrder = SupplierOrder.objects.filter(id=supplierOrder_id)
    products = Product.objects.filter(supplierOrder=supplierOrder).order_by('-id')
    paginator = StandardPagination()
    result_page = paginator.paginate_queryset(products, request)
    serializer = SupplierOrderProductSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)        



#supplier Order Product List View 

@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def supplierOrderProductListView(request):
    if request.method == "GET":
        supplier_order_products = SupplierOrderProduct.objects.all().order_by('-id')
        serializer = SupplierOrderProductSerializer(supplier_order_products, many=True)
        return Response(serializer.data)










# filtering

# class searchSupplier(generics.ListAPIView):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializer
#     filter_backends = [DjangoFilterBackend]
#     filter_class = ['supplier_name']
#     pagination_class = StandardPagination
    
    
# class searchSupplier(generics.ListAPIView):
#     queryset = Supplier.objects.filter('supplier_name__contains').order_by('id')
#     serializer_class = SupplierSerializer
#     # filter_backends = [DjangoFilterBackend, SearchFilter]
#     # filterset_fields = ['supplier_name']
#     # search_fields = ['supplier_name']
#     pagination_class = StandardPagination

class searchSupplier(generics.ListAPIView):
    queryset = Supplier.objects.all().order_by('-id')
    serializer_class = SupplierSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['supplier_name']

class searchSupplierOrderNumber(generics.ListAPIView):
    queryset = SupplierOrder.objects.all().order_by('-id')
    serializer_class = SupplierOrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_number']

class searchSupplierOrderProduct(generics.ListAPIView):
    queryset = SupplierOrderProduct.objects.all().order_by('-id')
    serializer_class = SupplierOrderProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order']
    


    
    
    




# Debit Credit information of Supplier

@api_view(["GET"])
def supplierAllDebitCreditInfo(request):
    if request.method == "GET":
        data = DebitCreditSupplier.objects.all().order_by('-id')
        paginator = StandardPagination()
        result_page = paginator.paginate_queryset(data, request)
        serializer = DebitCreditSupplierSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)



@api_view(['GET'])
def supplierDebitCreditDetail(request,pk):
    debit_credit = DebitCreditSupplier.objects.get(id=pk)
    serializer = DebitCreditSupplierSerializer(debit_credit)
    return Response(serializer.data)




@api_view(['DELETE'])
def supplierDebitCreditDelete(request, pk):
    debit_credit = DebitCreditSupplier.objects.get(id=pk)
    debit_credit.delete()
    return Response({"message":"Supplier Debit Credit DELETED successfully"})

        
    
# filter for dates
# @api_view(['GET'])
# def supplier_orders_weekly(request, supplier_id):
#     orders = filter_orders_weekly(supplier_id)
#     serializer = SupplierOrderSerializer(orders, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def supplier_orders_monthly(request, supplier_id):
#     orders = filter_orders_monthly(supplier_id)
#     serializer = SupplierOrderSerializer(orders, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def supplier_orders_yearly(request, supplier_id):
#     orders = filter_orders_yearly(supplier_id)
#     serializer = SupplierOrderSerializer(orders, many=True)
#     return Response(serializer.data)

class SupplierOrderListView(generics.ListAPIView):
    queryset = SupplierOrder.objects.all()
    serializer_class = SupplierOrderSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierOrderFilter
    
class searchSupplierInBalance(generics.ListAPIView):
    queryset = DebitCreditSupplier.objects.all().order_by('-id')
    serializer_class = DebitCreditSupplierSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['supplier']
    pagination_class = StandardPagination