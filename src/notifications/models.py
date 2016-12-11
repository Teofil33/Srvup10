from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

from .signals import notify

class Notification(models.Model):
	#sender = models.ForeignKey()
	#AUTH_USER_MODEL = 'accounts.MyUser'
	recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="notifications")
	action = models.CharField(max_length=333)

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return str(self.action) 


def new_notifications(sender, recipient, action, *args, **kwargs):
	print recipient
	print action
	print sender
	new_notification_create = Notification.objects.create(recipient=recipient, action=action)
	print args
	print kwargs

notify.connect(new_notifications)