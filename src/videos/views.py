from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

from notifications.signals import notify
from .models import Video, Category
from comments.models import Comment
from comments.forms import CommentForm

def video_detail(request, cat_slug, vid_slug):
	video = Video.objects.get(slug=vid_slug)
	category = video.category
	comments = Comment.objects.filter(video=video.id)
	form = CommentForm(request.POST or None)
	if form.is_valid():
		parent_id = request.POST.get("parent_id")
		parent_comment = None
		if parent_id:
			parent_comment = Comment.objects.get(id=parent_id)
		instance = form.save(commit=False)
		instance.user = request.user
		if parent_comment:
			instance.parent = parent_comment
		instance.video = video
		instance.path = request.get_full_path()
		instance.content = form.cleaned_data.get('content')
		instance.save()
		if parent_comment:
			notify.send(request.user, recipient=parent_comment.user, action="Responded to user")
			messages.success(request, "Thank you for your Reply!")
		else:
			notify.send(request.user, recipient=request.user, action="New comment added")
			messages.success(request, "Thank you for your Comment!")	
		return redirect(video.get_absolute_url())

	context = {
		"video": video,
		"category": category,
		"comments": comments,
		"form": form,
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



