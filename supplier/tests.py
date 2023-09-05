from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient



from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from .models import Supplier, SupplierOrder, SupplierOrderProduct
from product.models import Product  # Import the Product model from the correct location

class TestSearchOrderProductSupplier(APITestCase):

    def setUp(self):
        # Create a Supplier instance
        self.supplier = Supplier.objects.create(supplier_name='Supplier 1')

        # Create a SupplierOrder instance
        self.order = SupplierOrder.objects.create(
            order_number='123',
            supplier=self.supplier,
            phone='1234567890',
            email='supplier@example.com',
            order_note='Test order',
            invoice_date='2023-08-25T00:00:00Z',
            order_total=100.0
        )

        # Create a Product instance
        self.product = Product.objects.create(
            product_name='Product 1',
            product_description='Test product',
            selling_price=50,
            buying_price=30,
            supplier=self.supplier,
            stock=10,
            is_available=True
        )

        # Create a SupplierOrderProduct instance
        self.order_product = SupplierOrderProduct.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            product_price=50.0
        )

    def test_search_order_product_supplier(self):
        # URL of your API view
        
        supplier_url = reverse('supplier:search-order-product-supplier')
        response = self.client.get(supplier_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), SupplierOrderProduct.objects.count())
