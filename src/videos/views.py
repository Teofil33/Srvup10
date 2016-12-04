from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Video, Category

def video_detail(request, id):
	video = Video.objects.get(id=id)
	context = {
		"video": video,
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
def category_detail(request, slug=None):
	category = Category.objects.get(slug=slug)
	videos = category.video_set.all()
	context = {
		"category": category,
		"videos": videos,
	}
	return render(request, "category_detail.html", context)			



