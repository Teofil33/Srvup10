from django.contrib import admin

# Register your models here.

from .models import Video

class VideoAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "embed_code"]


admin.site.register(Video, VideoAdmin)	
