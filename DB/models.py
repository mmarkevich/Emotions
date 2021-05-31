from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=15)
    age = models.IntegerField(null=False, default=False)
    male = models.BooleanField(null=False, default=False)
    female = models.BooleanField(null=False, default=False)


class VideoInformation(models.Model):
    link = models.CharField(max_length=800)

    def __str__(self):
        return self.link


class DataAboutUserAndVideo(models.Model):
    ID_user = models.IntegerField(null=False, default=False)
    ID_video_information = models.IntegerField(null=False, default=False)
    ID_screenshot = models.IntegerField(null=False, default=False)
    second = models.DateTimeField(auto_now_add=True)
    neutral = models.IntegerField(null=False, default=False)
    surprise = models.IntegerField(null=False, default=False)
    sad = models.IntegerField(null=False, default=False)
    happy = models.IntegerField(null=False, default=False)
    fear = models.IntegerField(null=False, default=False)
    disgust = models.IntegerField(null=False, default=False)
    angry = models.IntegerField(null=False, default=False)
    dominant_emotion = models.CharField(max_length=50)
    edited_dominant_emotion = models.CharField(max_length=50)


class DominantEmotion(models.Model):
    dominant_emotion = models.CharField(max_length=15)