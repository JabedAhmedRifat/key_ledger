from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *

from rest_framework import status
from rest_framework.decorators import api_view ,authentication_classes
from knox.auth import TokenAuthentication

# from .filters import filter_orders_weekly, filter_orders_monthly, filter_orders_yearly

from .filters import CustomerOrderFilter

from .models import *

from customer.pagination import StandardPagination

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
# Create your views here.




@api_view(['GET'])
def productApiOverview(request):
    api_urls = {
        
        "Comment":"PRODUCT CRUD",
        'product List' : 'product/product-list/',
        'product Create' : 'product/product-create/',
        'product Update' : 'product/product-update/<int:pk>/',
        'product Delete' : 'product/product-delete/<int:pk>/',
        
        "Comment":"ORDER CRUD",
        'Order List' : 'product/order/list/',
        'Order Create' : 'product/order/create/',
        'Order Update' : 'product/order/update/<int:pk>/',
        'Order Delete' : 'product/order/delete/<int:pk>/',
        
        'Customer order product create and decrease stock' : 'product/order-product/create/',
        
        'supplier list': 'supplier/supplier-list/',
        'supplier create': 'supplier/supplier-create/',
        'supplier update': 'supplier/supplier-update/<int:pk>/',
        'supplier delete': 'supplier/supplier-delete/<int:pk>/',
        
        'supplier order list': 'supplier/supplier-list/',
        'supplier order create': 'supplier/supplier-create/',
        'supplier order update': 'supplier/supplier-update/<int:pk>/',
        'supplier order delete': 'supplier/supplier-delete/<int:pk>/',
        
        'supplier order product create': 'supplier/supplier-order-product/create/',
        
        'Customer list': 'customer/customer-list/',
        'Customer create': 'customer/customer-create/',
        'Customer update': 'customer/customer-update/<int:pk>/',
        'Customer delete': 'customer/customer-delete/<int:pk>/',
        
        
        
    }
    return Response(api_urls)





# product CRUD
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def allProductView(request):
    if request.method=="GET":
        data=Product.objects.all().order_by('-id')
        paginator = StandardPagination()
        result_page = paginator.paginate_queryset(data,request)
        serializer=ProductSerializer(result_page,many=True)
        return paginator.get_paginated_response(serializer.data)


    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def productDetail(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)



@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def productDelete(request, pk):
    product = Product.objects.get(id = pk )
    product.delete()
    return Response({
        'message': 'Product deleted successfully.'
    })



#Customer Order CRUD

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def allOrderView(request):
    if request.method == "GET":
        data = Order.objects.all().order_by('-id')
        paginator = StandardPagination()
        result_page = paginator.paginate_queryset(data, request)
        serializer = OrderSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def orderDetailView(request,pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(order)
    return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
def orderDeleteView(request,pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return Response({
        'message':'Order delete succssfully'
    })
    
    

            
            
# filter by customer order

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def productsInOrderView(request, order_id):
    order = OrderProduct.objects.filter(id=order_id)
    products = Product.objects.filter(order=order).order_by('-id')
    pagination = StandardPagination()
    paginated_products = pagination.paginate_queryset(products, request)
    serializer = orderProductSerializer(paginated_products, many=True)
    return pagination.get_paginated_response(serializer.data)
            
       
# Customer Order product list 
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def customerOrderProductListView(request):
    if request.method == "GET":
        supplier_order_products = OrderProduct.objects.all().order_by('-id')
        serializer = orderProductSerializer(supplier_order_products, many=True)
        return Response(serializer.data)
  

# Searching product_name from  Product Filtering 


class searchProductbyName(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name']
    
    
# Customer filtering  in order
    
class searchCustomerByOrder(generics.ListAPIView):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['customer']
    
    
# search order in order product of customer
class searchCustomerOrderProduct(generics.ListAPIView):
    queryset = OrderProduct.objects.all().order_by('-id')
    serializer_class = orderProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order']
    

#search supplier in product 

class searchProductBySupplier(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['supplier']

#search order_number in order of customer

class searchCustomerOrderNumber(generics.ListAPIView):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['order_number']
    



    
# filter for dates
# @api_view(['GET'])
# def customer_orders_weekly(request, customer_id):
#     orders = filter_orders_weekly(customer_id)
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def customer_orders_monthly(request, customer_id):
#     orders = filter_orders_monthly(customer_id)
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def customer_orders_yearly(request, customer_id):
#     orders = filter_orders_yearly(customer_id)
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)



class CustomerOrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_class = CustomerOrderFilter
    pagination_class = StandardPagination