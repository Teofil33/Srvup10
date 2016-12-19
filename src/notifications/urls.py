from django.conf.urls import include, url

from .views import notifications_list, read


urlpatterns = [
	url(r'^$', notifications_list, name="notification_list"),
	url(r'^read/(?P<id>\d+)/$', read, name="notification_read"),
	#url(r'^read/$', notifications_list, name="read")
	url(r'^unread/$', notifications_list, name="unread"),
	
]