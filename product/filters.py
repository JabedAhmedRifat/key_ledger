# from datetime import datetime, timedelta
# from django.db.models import Q
# from .models import Order

# def filter_orders_weekly(customer_id):
#     end_date = datetime.now()
#     start_date = end_date - timedelta(days=7)
#     return Order.objects.filter(
#         Q(customer_id=customer_id) &
#         Q(create_at__gte=start_date) &
#         Q(create_at__lte=end_date)
#     )

# def filter_orders_monthly(customer_id):
#     end_date = datetime.now()
#     start_date = end_date - timedelta(days=30)  # Adjust the number of days as needed
#     return Order.objects.filter(
#         Q(customer_id=customer_id) &
#         Q(create_at__gte=start_date) &
#         Q(create_at__lte=end_date)
#     )

# def filter_orders_yearly(customer_id):
#     end_date = datetime.now()
#     start_date = end_date - timedelta(days=365)  # Adjust the number of days as needed
#     return Order.objects.filter(
#         Q(customer_id=customer_id) &
#         Q(create_at__gte=start_date) &
#         Q(create_at__lte=end_date)
#     )


from django_filters import rest_framework as filters
from .models import Order

class CustomerOrderFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name='invoice_date', lookup_expr='date__gte')
    end_date = filters.DateFilter(field_name='invoice_date', lookup_expr='date__lte')

    class Meta:
        model = Order
        fields = ['start_date', 'end_date']
