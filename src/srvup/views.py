from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

from videos.models import Video
from .forms import LoginForm

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