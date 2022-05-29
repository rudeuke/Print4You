# views.py
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from register.forms import EditAddressForm
from register.forms import SetAddressForm
from register.forms import EditProfileForm
from register.forms import RegisterForm
from django.views import generic
from django.urls import reverse_lazy
from print4you.models import User


# Create your views here.

def homepage(request):
    return render(request, "homepage.html")

def homepage_redirect(request):
	return redirect("homepage")

def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Pomyślnie utworzono konto. Możesz się teraz zalogować.')
			return redirect("login")
	else:
		form = RegisterForm()	
	return render(request, "register.html", {"form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, f"Jesteś zalogowany jako {username}.")
				return redirect("homepage")
			else:
				messages.error(request,"Niewłaściwa nazwa użytkownika lub hasło.")
		else:
			messages.error(request,"Niewłaściwa nazwa użytkownika lub hasło.")
	form = AuthenticationForm()
	return render(request, "login.html", {"form":form})

class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('profile')

	

	def get_object(self):
		if self.request.method == "POST":
			messages.add_message(self.request, messages.INFO, 'Zapisano dane osobiste.')
		return self.request.user

	
def add_address(request):

	if request.user.is_authenticated:
		user = User.objects.get(pk=request.user.id)

	form = SetAddressForm(initial={"user":user})

	if request.method == 'POST':
		form = SetAddressForm(request.POST)
		messages.info(request, 'Zapisano dane adresu.')
		if form.is_valid():
			form.save()
	

	context = {'form':form}
	return render(request, 'registration/set_address.html', context)
	
class AddressEditView(generic.UpdateView):
	
	form_class = EditAddressForm
	template_name = 'registration/edit_address.html'
	success_url = reverse_lazy('profile')

	def get_object(self):
		if self.request.method == "POST":
			messages.add_message(self.request, messages.INFO, 'Zapisano dane adresu.')
		return self.request.user.address


def address_redirect(request):
	try:
		if request.user.address is not None:
			response = redirect('/edit_address/')
			return response
	except:
			response = redirect('/set_address/')
			return response







