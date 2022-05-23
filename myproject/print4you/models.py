from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

SIZE_CHOICES = (
    ('10x15', '10x15'),
    ('13x18', '13x18'),
    ('15x21', '15x21'),
    ('20x25', '20x25'),
    ('A4', 'A4'),
    ('A3', 'A3'),
    ('50x60', '50x60'),
    ('100x50', '100x50'),
    ('100x70', '100x70'),
    ('160x60', '160x60'),
    ('140x100', '140x100'),
    ('118 1mb', '118 1mb')
)

PAYMENT_CHOICS = (
    ('przelew', 'Przelew'),
    ('karta', 'Karta kredytowa/debetowa'),
    ('blik', 'BLIK')
)

DELIVERY_CHOICES = (
    ('poczta', 'Przesyłka pocztowa (+6,70zł)'),
    ('kurier', 'Przesyłka kurierska (+10,90zł)'),
    ('paczkomat', 'Odbiór w paczkomacie (+8,99zł)')
)


class Printout(models.Model):
    is_color = models.BooleanField(default=True)
    is_gloss = models.BooleanField(default=True)
    quantity = models.IntegerField(default=1)
    size = models.CharField(
        max_length=7,
        choices=SIZE_CHOICES,
        default='1'
    )
    image_file = models.ImageField(upload_to='user_prints')
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.price is None:
            if self.size == '10x15':
                pr = 0.5
            elif self.size == '13x18':
                pr = 1
            elif self.size == '15x21':
                pr = 1.5
            elif self.size == '20x25':
                pr = 4
            elif self.size == 'A4':
                pr = 6
            elif self.size == 'A3':
                pr = 10
            elif self.size == '50x60':
                pr = 20
            elif self.size == '100x50':
                pr = 35
            elif self.size == '100x70':
                pr = 45
            elif self.size == '160x60':
                pr = 60
            elif self.size == '140x100':
                pr = 90
            elif self.size == '118 1mb':
                pr = 40

            if self.is_gloss and self.is_color:
                pr = pr*1.2
            elif not self.is_gloss and not self.is_color:
                pr = pr*0.8
            elif self.is_gloss and not self.is_color:
                pr = pr*0.96

            pr = pr*self.quantity
            self.price = pr
            self.save()


class Address(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=60)
    home_number = models.CharField(max_length=8)
    postal_code = models.CharField(max_length=6)
    telephone_number = models.CharField(max_length=12)
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, blank=True, null=True)


class Order(models.Model):
    date = models.DateTimeField(auto_now=True)
    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_CHOICS,
        default='przelew'
    )
    delivery_method = models.CharField(
        max_length=30,
        choices=DELIVERY_CHOICES,
        default='poczta'
    )
    is_paid = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    printout = models.OneToOneField(Printout, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.cost == 0:
            if self.delivery_method == 'poczta':
                deliveryCost = 6.70
            elif self.delivery_method == 'kurier':
                deliveryCost = 10.90
            elif self.delivery_method == 'paczkomat':
                deliveryCost = 8.99

            totalCost = self.printout.price + Decimal(deliveryCost)
            self.cost = totalCost
            self.save()
