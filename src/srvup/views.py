from django.shortcuts import render

from videos.models import Video

def home(request):
	title = "Videos"
	videos = Video.objects.all()
	context = {
		"title": title,
		"videos": videos
	}
	return render(request, "videos.html", context)