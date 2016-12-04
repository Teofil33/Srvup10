from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Video(models.Model):
	title = models.CharField(max_length=333)
	embed_code = models.CharField(max_length=333, null=True, blank=True)

	def __unicode__(self):
		return self.title
