from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.category_list, name="categories"),
	url(r'^(?P<slug>[\w-]+)/$', views.category_detail, name="category_detail"),
	url(r'^(?P<id>\d+)/$', views.video_detail, name="video_detail"),

]