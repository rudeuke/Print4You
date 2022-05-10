# views.py
from ast import Add
from multiprocessing import context
from unicodedata import name
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from register.forms import EditAddressForm
from register.forms import EditProfileForm
from register.forms import RegisterForm
from django.views import generic
from django.urls import reverse_lazy
from print4you.models import User


# Create your views here.
def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
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
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("login")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "login.html", {"form":form})

class UserEditView(generic.UpdateView):
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('login')

	def get_object(self):
		return self.request.user

	
def add_address(request):

	if request.user.is_authenticated:
		user = User.objects.get(pk=request.user.id)

	form = EditAddressForm(initial={"user":user})

	if request.method == 'POST':
		form = EditAddressForm(request.POST)
		if form.is_valid():
			form.save()
	

	context = {'form':form}
	return render(request, 'registration/edit_address.html', context)
	

