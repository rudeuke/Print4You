from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=60)
    home_number = models.CharField(max_length=8)
    postal_code = models.CharField(max_length=6)


class Client(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    telephone_number = models.CharField(max_length=12)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=60)
    home_number = models.CharField(max_length=8)
    postal_code = models.CharField(max_length=6)


class Order(models.Model):
    date = models.DateTimeField(auto_now=True)
    payment_method = models.CharField(max_length=200)
    delivery_method = models.CharField(max_length=200)
    is_paid = models.BooleanField(default=False)
    cost = models.DecimalField(decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, primary_key=True)


class Printout(models.Model):
    color = models.BooleanField(default=True)
    material = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
