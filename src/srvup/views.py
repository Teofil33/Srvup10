from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

from videos.models import Video, Category
# from accounts.models import MyUser
# from .forms import LoginForm
# from accounts.forms import RegisterForm


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


def about(request):
	return render(request, "about.html", {})	

def contact(request):
	return render(request, "contact.html", {})






