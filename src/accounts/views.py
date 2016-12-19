from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

from notifications.signals import notify

# Create your views here.

from .models import MyUser
from .forms import LoginForm
from .forms import RegisterForm

def auth_register(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password2")
		email = form.cleaned_data.get("email")
		#MyUser.objects.create_user(username=username, email=email, password=password)
		new_user = MyUser()
		new_user.username = username
		new_user.email = email
		new_user.set_password(password)
		new_user.save()
		return redirect('login')

	context = {
		"form": form,
	}
	return render(request, "register.html", context)

def auth_login(request):
	form = LoginForm(request.POST or None)
	#next_url = request.GET.get("next")
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		#if user.is_authenticated():
		if user is not None:
			login(request, user)
			notify.send(request.user, recipient=request.user, verb="Logged In")
			return redirect("home")
	context = {
		"form": form
	}
	return render(request, "login.html", context)

def auth_logout(request):
	logout(request)
	return render(request, "logout.html", {})		


