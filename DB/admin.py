from django.contrib import admin
from .models import User, VideoInformation

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'password', 'male', 'female', 'age')
    list_display_links = ('id', 'nickname')
    search_fields = ('id', 'nickname')


admin.site.register(User, UserAdmin)


class VideoInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'link')
    list_display_links = ('id', 'link')


admin.site.register(VideoInformation, VideoInformationAdmin)
