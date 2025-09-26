from django.contrib import admin
from .models import Video, SiteUser

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'duration_minutes', 'published', 'created_at')
    search_fields = ('title','description','instructor')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(SiteUser)
class SiteUserAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','phone','created_at')
    search_fields = ('full_name','email')
