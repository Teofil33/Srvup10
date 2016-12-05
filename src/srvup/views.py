from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

from videos.models import Video, Category
from accounts.models import MyUser
from .forms import LoginForm
from accounts.forms import RegisterForm

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


@login_required(login_url='/login/')
def home(request):
	title = "Videos"
	videos = Video.objects.all()
	embeds = []
	for vid in videos:
		code = mark_safe(vid.embed_code)
		embeds.append("%s" %(code))
	context = {
		"title": title,
		"videos": videos,
		"embeds": embeds,
		"number": videos.count(),
	}
	return render(request, "videos.html", context)

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
			return redirect("home")
	context = {
		"form": form
	}
	return render(request, "login.html", context)

def auth_logout(request):
	logout(request)
	return render(request, "logout.html", {})

def about(request):
	return render(request, "about.html", {})	

def contact(request):
	return render(request, "contact.html", {})






