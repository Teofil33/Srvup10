from django.shortcuts import render

# Create your views here.

from .models import Video

def video_detail(request, id):
	video = Video.objects.get(id=id)
	context = {
		"video": video,
	}
	return render(request, "video_detail.html", context)



