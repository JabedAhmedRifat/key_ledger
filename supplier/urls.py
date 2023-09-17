from django.urls import path
from .views import *
from .postviews import *
from . import views


urlpatterns=[
    # for supplier
    path('supplier-list/', allSupplierView),
    path('supplier-create/', createSupplierView),
    path('supplier-detail/<int:pk>/', supplierDetail),
    path('supplier-update/<int:pk>/', supplierUpdate),
    path('supplier-delete/<int:pk>/', supplierDelete),



    # for supplier Order
    path('supplier-order/list/', allSupplierOrderView),
    path('supplier-order/detail/<int:pk>/', supplierOrderDetailView),
    path('supplier-order/create/', createSupplierOrderView),
    path('supplier-order/update/<int:pk>/', supplierOrderUpdateView),
    path('supplier-order/delete/<int:pk>/', supplierOrderDeleteView),
    
    
    #for supplier order product
    path('supplier-order-product/create/', createSupplierOrderProductView),
    path('supplier-order-product/list/', supplierOrderProductListView),

    #filtering using supplier_name
    path('search-supplier/',searchSupplier.as_view()),
    
    #filtering using order in supplierOrderProduct
    path('search-supplier-order-product/', searchSupplierOrderProduct.as_view()),
    
    # filtering using order_number in SupplierOrder
    path('search-supplier-order-number/', searchSupplierOrderNumber.as_view()),
    
    #Supplier Debit Credit Balance 
    path('supplier-balance/list/', supplierAllDebitCreditInfo),
    path('supplier-balance/detail/<int:pk>/', supplierDebitCreditDetail),
    path('supplier-balance/create/', createSupplierDebitCredit),
    path('supplier-balance/update/<int:pk>/', supplierDebitCreditUpdate),
    path('supplier-balance/delete/<int:pk>/', supplierDebitCreditDelete),
    
    
    # filter for dates
    # path('<int:supplier_id>/orders/weekly/', views.supplier_orders_weekly, name='supplier_orders_weekly'),
    # path('<int:supplier_id>/orders/monthly/', views.supplier_orders_monthly, name='supplier_orders_monthly'),
    # path('<int:supplier_id>/orders/yearly/', views.supplier_orders_yearly, name='supplier_orders_yearly'),
    path('supplier-order/', views.SupplierOrderListView.as_view(), name='supplier-order-list'),
    path('search-supplier-balance/' ,searchSupplierInBalance.as_view()),

    path('search-supplier-from-supplier-order/', searchSupplierFromSupplierOrder.as_view()),

]
