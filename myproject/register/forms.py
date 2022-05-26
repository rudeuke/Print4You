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
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class SetAddressForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    street = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    home_number = forms.CharField(
        max_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}))
    postal_code = forms.CharField(
        max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone_number = forms.CharField(
        max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Address
        fields = ["first_name", "last_name", "email", "city", "street",
                  "home_number", "postal_code", "telephone_number", "user"]
