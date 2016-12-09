from django.contrib import admin

# Register your models here.

from .models import Comment

class CommmentAdmin(admin.ModelAdmin):
	list_display = ['user', 'video', '__unicode__', 'timestamp']

admin.site.register(Comment)
