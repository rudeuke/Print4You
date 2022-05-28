from django import forms
from django.forms import ModelForm
from print4you.models import Printout, Order, Address


class PrintoutForm(ModelForm):
    class Meta:
        model = Printout
        fields = ['is_color', 'is_gloss', 'quantity', 'size', 'image_file']
        labels = {
            'is_color': ('Kolor'),
            'is_gloss': ('Połysk'),
            'quantity': ('Ilość'),
            'size': ('Format'),
            'image_file': ('Plik graficzny'),
        }


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method', 'delivery_method']
        labels = {
            'payment_method': ('Metoda płatności'),
            'delivery_method': ('Sposób dostawy'),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["first_name", "last_name", "email", "city",
                  "street", "home_number", "postal_code", "telephone_number"]
        labels = {
            'first_name': ('Imię'),
            'last_name': ('Nazwisko'),
            'email': ('Email'),
            'city': ('Miasto'),
            'street': ('Ulica'),
            'home_number': ('Numer domu'),
            'postal_code': ('Kod pocztowy'),
            'telephone_number': ('Numer telefonu'),
        }
