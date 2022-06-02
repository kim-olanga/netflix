from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import uuid

AGE_CHOICES=(
    ('All','All'),
    ('kids','kids')
)
MOVIE_CHOICES=(
    ('seasonal','seasonal'),
    ('single','Single')
)

# Create your models here.
class User(models.Model):
    profiles = models.ManyToManyField('profile',null=True,blank=True)

    def __str__(self):
        return self.profiles

class Profile(models.Model):
    name = models.CharField(max_length=200)
    age_limit = models.CharField(max_length=100,choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4) #help request for a particular model

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=100,choices=MOVIE_CHOICES)
    vedios = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=100,choices=AGE_CHOICES)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=300,blank=True,null=True)
    file = models.FieldFile(upload_to='movie')

    def __str__(self):
        return self.title