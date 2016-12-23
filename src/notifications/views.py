import json

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, Http404, HttpResponseRedirect

# Create your views here.

from .models import Notification


@login_required
def notifications_list(request):
	#notifications = Notification.objects.all().get_user(request.user)
	notifications = Notification.objects.all_for_user(request.user)
	context = {
		"notifications": notifications,
	}
	return render(request, "notifications.html", context)

@login_required
def read(request, id):
	next = request.GET.get('next', None)
	notification = Notification.objects.get(id=id)
	if notification.recipient == request.user:
		notification.read = True
		notification.save()
		if next is not None:
			return HttpResponseRedirect(next)
		else:
			return HttpResponseRedirect(reverse("notifications:notification_list"))	
	else:
		raise Http404


@login_required
def get_notifications_ajax(request):
	notifications = Notification.objects.all_for_user(request.user).recent()
	count = notifications.count()
	notes = []
	for note in notifications:
		notes.append(str(note.get_link))
	data = {
		"notifications": notes,
		"count": count,
	}
	json_data = json.dumps(data)
	return HttpResponse(json_data, content_type="application/json")				
