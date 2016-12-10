from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Comment
from videos.models import Video, Category
from comments.forms import CommentForm

@login_required
def comment_thread(request, id, cat_slug, vid_slug):
	comment = Comment.objects.get(id=id)
	video = Video.objects.get(slug=vid_slug)
	category = Category.objects.get(slug=cat_slug)
	comment_form = CommentForm(request.POST or None)
	if comment_form.is_valid():
		#parent_id = comment.id
		parent_comment = comment
		instance = comment_form.save(commit=False)
		instance.user = request.user
		instance.parent = parent_comment
		instance.video = video
		instance.path = request.get_full_path()
		instance.content = comment_form.cleaned_data.get("content")
		instance.save()
		return redirect(comment.get_absolute_url())
	context = {
		"comment": comment,
		"video": video,
		"category": category,
		"form": comment_form
	}
	return render(request, "comment_thread.html", context)


