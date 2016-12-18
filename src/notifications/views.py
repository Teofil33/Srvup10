from django.shortcuts import render

# Create your views here.

from .models import Notification

def notifications_list(request):
	notifications = Notification.objects.all().get_user(request.user)
	#notifications = Notification.objects.all_for_user(request.user)
	context = {
		"notifications": notifications,
	}
	return render(request, "notifications.html", context)
