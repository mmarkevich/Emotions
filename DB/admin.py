from django.contrib import admin
from .models import VideoInformation

# Register your models here.



class VideoInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'link')
    list_display_links = ('id', 'link')


admin.site.register(VideoInformation, VideoInformationAdmin)
