from django.db import models
from django.conf import settings




class VideoInformation(models.Model):
    link = models.CharField(max_length=800)

    def str(self):
        return self.link


class DataAboutUserAndVideo(models.Model):
    ID_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ID_video_information = models.CharField(max_length=80)
    dominant_emotion = models.CharField(max_length=50)
    edited_dominant_emotion = models.CharField(max_length=50)