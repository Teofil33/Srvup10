from __future__ import unicode_literals
from django.shortcuts import reverse
from django.db import models

# Create your models here.

class VideoQueryset(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)
	def featured(self):
		return self.filter(featured=True)	

class VideoManager(models.Manager):
	def get_queryset(self):
		return VideoQueryset(self.model, using=self._db)

	def get_featured(self):
		return self.get_queryset().active().featured()

	def get_active(self):
		return self.get_queryset().active()

	def all(self):			
		return self.get_queryset().active()

		
class Video(models.Model):
	title = models.CharField(max_length=333)
	embed_code = models.CharField(max_length=333, null=True, blank=True)
	active = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	free_preview = models.BooleanField(default=False)

	objects = VideoManager()

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("videos:video_detail", kwargs={"id": self.id})	
