from django import template
from product.models import Discount


register = template.Library()


@register.simple_tag
def discounts(slug):
    discount = Discount.objects.filter(product__slug=slug, is_active=True)
    if discount:
        return discount[0].profit_value(discount[0].product.price)
    else:
        return f"Not Today"
