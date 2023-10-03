from rest_framework.response import Response
from .serializers import *


from rest_framework.decorators import api_view , authentication_classes
from knox.auth import TokenAuthentication


from .models import *
from product.models import Product
from product.serializers import ProductSerializer
# Create your views here


# supplier CRUD

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
def createSupplierView(request):
        data=request.data
        supplier_name = data.get('supplier_name', None)
        if supplier_name is not None:
            existing_supplier = Supplier.objects.filter(supplier_name__iexact=supplier_name).exists()
            
            if existing_supplier:
                return Response({'error':'Supplier with this name already Exist'})
            
        serializer=SupplierSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    

    
    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def supplierUpdate(request, pk):
    supplier = Supplier.objects.get(id = pk)
    serializer = SupplierSerializer(instance=supplier, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



# supplier order CRUD



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def createSupplierOrderView(request):
    data =request.data
    serializer = SupplierOrderSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# @api_view(["POST"])
# @authentication_classes([TokenAuthentication])
# def createSupplierOrderView(request):
#     data = request.data
#     serializer = SupplierOrderSerializer(data=data)  
#     if serializer.is_valid():
#         supplier_order_instance = serializer.save()
#         supplier_order_instance.order_number = f'dsa{supplier_order_instance.id}'
#         supplier_order_instance.save() 
#         return Response(serializer.data)
#     return Response(serializer.errors)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def supplierOrderUpdateView(request,pk):
    supplierOrder = SupplierOrder.objects.get(id=pk)
    serializer = SupplierOrderSerializer(instance=supplierOrder,data = request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# supplier Order Product Stock change
# @api_view(["GET"])
# @authentication_classes([TokenAuthentication])
# def supplierOrderProductList(request):




@api_view(["POST"])
@authentication_classes([TokenAuthentication])
def createSupplierOrderProductView(request):
    product_id = request.data['product']
    quantity = int(request.data['quantity'])

    stock_product = Product.objects.get(id=product_id)
    stock_serializer = ProductSerializer(stock_product)

    total_stock = int(stock_serializer.data['stock'])
    print(total_stock)
    data = request.data
    serializer = SupplierOrderProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

        stock_product.stock = total_stock + quantity
        stock_product.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)



# Debit Credit information of Supplier

@api_view(["POST"])
def createSupplierDebitCredit(request):
    data = request.data
    serializer = DebitCreditSupplierSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)



@api_view(['POST'])
def supplierDebitCreditUpdate(request,pk):
    debit_credit = DebitCreditSupplier.objects.get(id=pk)
    serializer = DebitCreditSupplierSerializer(instance=debit_credit, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


