from django.test import TestCase
from product.models import Discount, Product


class DiscountTest(TestCase):
    def setUp(self) -> None:
        self.discount1 = Discount.objects.create(value=20, type='percent')
        self.discount2 = Discount.objects.create(value=5000, type='price')
        self.discount3 = Discount.objects.create(value=30, type='percent', max_price='10000')

    def test1_profit_price10000(self):
        self.assertEqual(self.discount1.profit_value(10000), 2000)
        self.assertEqual(self.discount2.profit_value(10000), 5000)
        self.assertEqual(self.discount3.profit_value(10000), 3000)

    def test2_profit_price100000(self):
        self.assertEqual(self.discount1.profit_value(100000), 20000)
        self.assertEqual(self.discount2.profit_value(100000), 5000)
        self.assertEqual(self.discount3.profit_value(100000), 10000)

    def test3_profit_price7000(self):
        self.assertEqual(self.discount1.profit_value(7000), 1400)
        self.assertEqual(self.discount2.profit_value(7000), 5000)
        self.assertEqual(self.discount3.profit_value(7000), 2100)

    def test4_profit_price7111(self):
        self.assertEqual(self.discount1.profit_value(7111), 1422)
        self.assertEqual(self.discount2.profit_value(7111), 5000)
        self.assertEqual(self.discount3.profit_value(7111), 2133)

    def test5_profit_price2000(self):
        self.assertEqual(self.discount1.profit_value(2000), 400)
        self.assertEqual(self.discount2.profit_value(2000), 2000)
        self.assertEqual(self.discount3.profit_value(2000), 600)


class ProductTest(TestCase):
    def setUp(self) -> None:
        self.product1 = Product.objects.create(name='p1', discount=Discount.objects.create(type='percent', value=30, max_price=100), price=500, stock=10)
        self.product2 = Product.objects.create(name='p2', discount=Discount.objects.create(type='price', value=100), price=5000, stock=10)
        self.product3 = Product.objects.create(name='p3', discount=Discount.objects.create(type='percent', value=50, max_price=4000), price=10000, stock=10)

    def test1_product_price(self):
        self.assertEqual(self.product1.product_price(), 400)
        self.assertEqual(self.product2.product_price(), 4900)
        self.assertEqual(self.product3.product_price(), 6000)

    def test1_del_discount(self):
        self.assertEqual(self.product1.del_discount(), True)
        self.assertEqual(self.product2.del_discount(), True)
        self.assertEqual(self.product3.del_discount(), True)

    def test1_add_discoount(self):
        self.assertEqual(self.product1.add_discount(1), True)
        self.assertEqual(self.product2.add_discount(2), True)
        self.assertEqual(self.product3.add_discount(3), True)
