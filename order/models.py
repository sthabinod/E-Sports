from django.db import models
from product.models import Product
from accounts.models import Customer
from django.contrib.auth.models import User


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    street = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    order_date = models.DateTimeField(null=True, blank=True)
    order_status = models.BooleanField(null=True, default=False)
    complete = models.BooleanField(default=False)
    payment_status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Sales/Order'
        verbose_name_plural = 'Sales/Order'


class Wishlist(models.Model):
    customer = models.ForeignKey(
        User, related_name='products', on_delete=models.CASCADE)

    product = models.ForeignKey(
        Product, related_name='products', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('customer', 'product',)
        verbose_name_plural = 'Wishlist'
