from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from httpx import Auth
from requests import request
from print4you.models import Address


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
        labels = {
            'username': ('Nazwa użytkownika'),
            'email': ('Adres e-mail'),
            'first_name': ('Imię'),
            'last_name': ('Nazwisko'),
    }

class SetAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["first_name", "last_name", "email", "city", "street", "home_number", "postal_code", "telephone_number", "user"]
        labels = {
            'first_name': ('Imię'),
            'last_name': ('Nazwisko'),
            'email': ('Adres e-mail'),
            'city': ('Miasto'),
            'street': ('Ulica'),
            'home_number': ('Numer domu'),
            'postal_code': ('Kod pocztowy'),
            'telephone_number': ('Numer telefonu'),
            }
        widgets = {'user': forms.HiddenInput()}

class EditAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["first_name", "last_name", "email", "city", "street", "home_number", "postal_code", "telephone_number", "user"]
        labels = {
            'first_name': ('Imię'),
            'last_name': ('Nazwisko'),
            'email': ('Adres e-mail'),
            'city': ('Miasto'),
            'street': ('Ulica'),
            'home_number': ('Numer domu'),
            'postal_code': ('Kod pocztowy'),
            'telephone_number': ('Numer telefonu'),
            }
        widgets = {'user': forms.HiddenInput()}
