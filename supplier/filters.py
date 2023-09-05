# from datetime import datetime, timedelta
# from django.db.models import Q
# from .models import SupplierOrder

# def filter_orders_weekly(supplier_id):
#     end_date = datetime.now()
#     start_date = end_date - timedelta(days=7)
#     return SupplierOrder.objects.filter(
#         Q(supplier_id=supplier_id) &
#         Q(create_at__gte=start_date) &
#         Q(create_at__lte=end_date)
#     )

# def filter_orders_monthly(supplier_id):
#     end_date = datetime.now()
#     start_date = end_date - timedelta(days=30)  # Adjust the number of days as needed
#     return SupplierOrder.objects.filter(
#         Q(supplier_id=supplier_id) &
#         Q(create_at__gte=start_date) &
#         Q(create_at__lte=end_date)
#     )

# def filter_orders_yearly(supplier_id):
#     end_date = datetime.now()
#     start_date = end_date - timedelta(days=365)  # Adjust the number of days as needed
#     return SupplierOrder.objects.filter(
#         Q(supplier_id=supplier_id) &
#         Q(create_at__gte=start_date) &
#         Q(create_at__lte=end_date)
#     )



from django_filters import rest_framework as filters
from .models import SupplierOrder

class SupplierOrderFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name='invoice_date', lookup_expr='date__gte')
    end_date = filters.DateFilter(field_name='invoice_date', lookup_expr='date__lte')

    class Meta:
        model = SupplierOrder
        fields = ['start_date', 'end_date']
