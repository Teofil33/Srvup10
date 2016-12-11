from django.conf.urls import include, url

from .views import notifications_list


urlpatterns = [
	url(r'^$', notifications_list, name="notification_list")
]