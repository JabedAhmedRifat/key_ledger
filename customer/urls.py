from django.urls import path
from .views import *
from .postviews import *

urlpatterns=[
    path('customer-list/', allCustomerView),
    path('customer-create/', createCustomerView),
    path('customer-detail/<int:pk>/', customerDetail),
    path('customer-update/<int:pk>/', customerUpdate),
    path('customer-delete/<int:pk>/', customerDelete),
    
    #filtering
    path('search-customer/', searchCustomer.as_view()),


    #Customer Debit Credit Balance
    path('customer-balance/list/', customerAllDebitCreditInfo),
    path('customer-balance/detail/<int:pk>/', customerDebitCreditDetail),
    path('customer-balance/create/', createCustomerDebitCredit),
    path('customer-balance/update/<int:pk>/', customerDebitCreditUpdate),
    path('customer-balance/delete/<int:pk>/', customerDebitCreditDelete),

    path('search-customer-balance/' ,searchCustomerInBalance.as_view()),
]