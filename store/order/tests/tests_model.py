from django.test import TestCase
from order.models import Basket, Order
from product.models import Product


class BasketTest(TestCase):
    def setUp(self):
        self.basket1 = Basket.objects.create(product=Product.objects.create(name='p1', price=500, stock=10), order=Order.objects.create(), quantity=3)

    def test1_basket_item_price(self):
        self.assertEqual(self.basket1.basket_item_price(), 1500)
