from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings

# Create your models here.

from .signals import notify

class Notification(models.Model):
	# Someone did something, AUTH_USER_MODEL

	# video, category type of model, name of model related to
	sender_content_type = models.ForeignKey(ContentType, related_name='notify_sender')
	sender_object_id = models.PositiveIntegerField()
	# specific Video object with it, title, being related to first two fields
	sender_object = GenericForeignKey("sender_content_type", "sender_object_id")

	verb = models.CharField(max_length=255)

	# Created a Comment/Reply on video or comment

	action_content_type = models.ForeignKey(ContentType, related_name='notify_action', null=True, blank=True)
	action_object_id = models.PositiveIntegerField(null=True, blank=True)
	action_object = GenericForeignKey("action_content_type", "action_object_id")

	# Target -> video or parent comment

	target_content_type = models.ForeignKey(ContentType, related_name='notify_target', null=True, blank=True)
	target_object_id = models.PositiveIntegerField(null=True, blank=True)
	target_content_object = GenericForeignKey("target_content_type", "target_object_id")	

	recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="notifications")

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return str(self.verb)

	class Meta:
		ordering = ["-timestamp"]	 


def new_notifications(sender, **kwargs):
	print(kwargs)
	kwargs.pop('signal', None)
	recipient = kwargs.pop("recipient")
	verb = kwargs.pop("verb")
	# target = kwargs.pop('target', None)
	# action = kwargs.pop('action', None)
	new_note = Notification(
		recipient = recipient,
		verb=verb,
		sender_content_type = ContentType.objects.get_for_model(sender),
		sender_object_id = sender.id
	)

	for option in ("target", "action"):
		obj = kwargs.pop(option, None)
		if obj is not None:
			setattr(new_note, "%s_content_type" %option, ContentType.objects.get_for_model(obj))
			setattr(new_note, "%s_object_id" %option, obj.id)

	# if target is not None:
	# 	new_note.target_content_type = ContentType.objects.get_for_model(target)
	# 	new_note.target_object_id = target.id
	# if action is not None:
	# 	new_note.action_content_type = ContentType.objects.get_for_model(action)
	# 	new_note.action_object_id = action.id

	new_note.save()

notify.connect(new_notifications)








