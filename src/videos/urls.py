from django.conf.urls import url

from . import views
from comments.views import comment_thread

urlpatterns = [
	url(r'^$', views.category_list, name="categories"),
	url(r'^(?P<cat_slug>[\w-]+)/$', views.category_detail, name="category_detail"),
	url(r'^(?P<cat_slug>[\w-]+)/(?P<vid_slug>[\w-]+)/$', views.video_detail, name="video_detail"),
	url(r'^(?P<cat_slug>[\w-]+)/(?P<vid_slug>[\w-]+)/(?P<id>\d+)/$', comment_thread, name="comment_thread"),

]