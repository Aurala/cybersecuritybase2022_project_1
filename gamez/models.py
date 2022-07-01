from django.db import models
from django.contrib.auth.models import User
from django.forms import BooleanField


# Just the very basic fields. This app is not meant for the use of a real collector. :)

class Platform(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(null=True)
    gen = models.IntegerField(null=True)

class Collection(models.Model):
    user = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=64)

class Game(models.Model):
    collection = models.ForeignKey(Collection, default=0, on_delete=models.CASCADE)
    thumbnail = models.CharField(max_length=250, default='')
    info = models.CharField(max_length=250, default='')
    name = models.CharField(max_length=50)
    platform = models.ForeignKey(Platform, default=0, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True)
