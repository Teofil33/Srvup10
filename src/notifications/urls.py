from django.conf.urls import include, url

from .views import notifications_list, read, get_notifications_ajax


urlpatterns = [
	url(r'^$', notifications_list, name="notification_list"),
	url(r'^ajax/$', get_notifications_ajax, name="get_notifications_ajax"),
	url(r'^read/(?P<id>\d+)/$', read, name="notification_read"),
	#url(r'^read/$', notifications_list, name="read")
	url(r'^unread/$', notifications_list, name="unread"),
	
]