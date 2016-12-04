from __future__ import unicode_literals
from django.shortcuts import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	slug_qs = Category.objects.filter(slug=slug).order_by("-id")
	if slug_qs.exists():
		new_slug = "%s-%s" %(slug, slug_qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug		

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
	category = models.ForeignKey("Category", null=True)
	active = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	free_preview = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	objects = VideoManager()

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("videos:video_detail", kwargs={"id": self.id})	


class Category(models.Model):
	title = models.CharField(max_length=333)
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to="images/", null=True, blank=True)
	slug = models.SlugField(unique=True)
	active = models.BooleanField(default=True)
	featured = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("videos:category_detail", kwargs={"slug": self.slug})	


def pre_save_category_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_category_receiver, sender=Category)				








