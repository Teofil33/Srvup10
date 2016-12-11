from django.contrib import admin

# Register your models here.

from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
	list_display = ["__unicode__"]


admin.site.register(Notification, NotificationAdmin)	
