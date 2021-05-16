from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length=10)
    password = models.CharField(max_length=8)
    age = models.IntegerField(null=False, default=False)
    male = models.BooleanField(null=False, default=False)
    female = models.BooleanField(null=False, default=False)