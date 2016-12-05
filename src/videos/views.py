from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Video, Category

def video_detail(request, cat_slug, vid_slug):
	video = Video.objects.get(slug=vid_slug)
	category = video.category
	context = {
		"video": video,
		"category": category,
	}
	return render(request, "video_detail.html", context)

@login_required
def category_list(request):
	categories = Category.objects.all()
	context = {
		"categories": categories,
	}
	return render(request, "categories.html", context)

@login_required
def category_detail(request, cat_slug=None):
	category = Category.objects.get(slug=cat_slug)
	videos = category.video_set.all()
	context = {
		"category": category,
		"videos": videos,
	}
	return render(request, "category_detail.html", context)			



