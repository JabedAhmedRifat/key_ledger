from django.urls import path
from .views import *
from .postviews import *
from . import views

urlpatterns=[
    
    path('', productApiOverview),
    # for product
    path('product-list/', allProductView),    
    path('product-create/', createProductView),
    path('product-detail/<int:pk>/', productDetail),
    path('product-update/<int:pk>/', productUpdate),
    path('product-delete/<int:pk>/', productDelete),
    
    
    # for order
    path('order/list/', allOrderView),
    path('order/create/', createOrderView),
    path('order/detail/<int:pk>/', orderDetailView),
    path('order/update/<int:pk>/', orderUpdateView),
    path('order/delete/<int:pk>/', orderDeleteView),
    
    # Customer  order Product  for decrease stock
    path ('order-product/create/', CustomerCreateOrderProductView),
    path('order-product/list/', customerOrderProductListView),
    
    #filtering
    path('search-product/', searchProductbyName.as_view()),
    
    path('search-customer/',searchCustomerByOrder.as_view()),
    
    #filtering Customer Order Product
    path('search-order-product-customer/', searchCustomerOrderProduct.as_view()),
    
    path("search-supplier/" , searchProductBySupplier.as_view()),
    
    #filter order_number for customer from Order 
    path('search-customer-order-number/', searchCustomerOrderNumber.as_view()),
    
    
    # filter for dates
    # path('<int:customer_id>/orders/weekly/', views.customer_orders_weekly, name='supplier_orders_weekly'),
    # path('<int:customer_id>/orders/monthly/', views.customer_orders_monthly, name='supplier_orders_monthly'),
    # path('<int:customer_id>/orders/yearly/', views.customer_orders_yearly, name='supplier_orders_yearly'),
    
    path('customer-order/', views.CustomerOrderListView.as_view()),

    path('search-customer-from-customer-order/', searchCustomerFromCustomerOrder.as_view()),

]
