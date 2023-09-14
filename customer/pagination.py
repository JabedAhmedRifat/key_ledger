from rest_framework.pagination import PageNumberPagination

class StandardPagination(PageNumberPagination):
    page_size=15
    page_query_param='page_number'