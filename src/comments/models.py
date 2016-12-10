from __future__ import unicode_literals

from django.db import models
from django.shortcuts import reverse
from accounts.models import MyUser
from videos.models import Video

# Create your models here.

# class CommentManager(models.Manager):
# 	def all(self):
# 		return super(CommentManager, self).filter(active=True).filter(parent=None) # .order_by("-timestamp")

# 	def create_comment(self, user=None, content=None, parent=None, video=None):
# 		if not path:
# 			raise ValueError("Must include path when adding a comment")
# 		if not user:
# 			raise ValueError("Must specify user when adding a comment")

# 		comment = self.model(
# 				user = user,
# 				path = path,
# 				content = content
# 			)

# 		if video is not None:
# 			comment.video = video

# 		if parent is not None:
# 			comment.parent = parent

# 		comment.save(using=self._db)
# 		return comment					

			

class Comment(models.Model):
	user = models.ForeignKey(MyUser)
	parent = models.ForeignKey("self", null=True, blank=True)
	content = models.TextField()
	path = models.CharField(max_length=333, null=True, blank=True)
	video = models.ForeignKey(Video)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=True, auto_now=False)
	active = models.BooleanField(default=True)


	class Meta:
		ordering = ["-timestamp"]

	def __unicode__(self):
		return self.content

	def get_absolute_url(self):
		return reverse("videos:comment_thread", kwargs = {"cat_slug": self.video.category.slug, "vid_slug": self.video.slug, "id": self.id})	

	@property
	def get_comment(self):
		return self.content	

	def is_parent(self):
		if self.parent is None:
			return True
		else:
			return False

	def is_child(self):
		if self.parent is not None:
			return True
		else:
			return False

	def get_children(self):
		if self.is_child():
			return None
		else:
			return Comment.objects.filter(parent=self)








