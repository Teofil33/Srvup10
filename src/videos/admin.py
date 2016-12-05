from django.contrib import admin

# Register your models here.

from .models import Video, Category

class VideoAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "embed_code"]
	prepopulated_fields = {'slug': ['title']}

class CategoryAdmin(admin.ModelAdmin):
	list_display = ["__unicode__"]	


admin.site.register(Video, VideoAdmin)

admin.site.register(Category, CategoryAdmin)	
