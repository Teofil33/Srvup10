from django.shortcuts import render

# Create your views here.

from .models import Notification

def notifications_list(request):
	notifications = Notification.objects.all()
	context = {
		"notifications": notifications,
	}
	return render(request, "notifications.html", context)
