from __future__ import unicode_literals

from django.db import models

from accounts.models import MyUser
from videos.models import Video

# Create your models here.

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








