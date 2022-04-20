from django.db import models
from django.contrib.auth.models import User


class Printout(models.Model):
    is_color = models.BooleanField(default=True)
    is_gloss = models.BooleanField(default=True)
    quantity = models.IntegerField(default=1)
    image_file = models.ImageField(upload_to='user_prints')
    price = models.DecimalField(max_digits=9, decimal_places=2)


class Address(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=60)
    home_number = models.CharField(max_length=8)
    postal_code = models.CharField(max_length=6)
    telephone_number = models.CharField(max_length=12)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)


class Order(models.Model):
    date = models.DateTimeField(auto_now=True)
    payment_method = models.CharField(max_length=200)
    delivery_method = models.CharField(max_length=200)
    is_paid = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    printout = models.OneToOneField(Printout, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
