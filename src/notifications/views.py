from django.core.urlresolvers import reverse
from django.shortcuts import render, Http404, HttpResponseRedirect

# Create your views here.

from .models import Notification

def notifications_list(request):
	#notifications = Notification.objects.all().get_user(request.user)
	notifications = Notification.objects.all_for_user(request.user)
	context = {
		"notifications": notifications,
	}
	return render(request, "notifications.html", context)

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
