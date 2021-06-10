from django.db import models
from django.conf import settings

class DB_VideoInformation(models.Model):
    link = models.CharField(max_length = 80)

class DataAboutUserAndVideo(models.Model):
    ID_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ID_video_information = models.ForeignKey(DB_VideoInformation, on_delete=models.CASCADE)
    dominant_emotion = models.CharField(max_length=50)
    edited_dominant_emotion = models.CharField(max_length=50)
    time_emo = models.TimeField(max_length=40, null=True)



