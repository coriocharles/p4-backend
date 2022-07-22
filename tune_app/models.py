import time
from datetime import date
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.ImageField(upload_to='tune_app')
    bio = models.TextField(default='')
    birthday = models.DateField(default=date.today)
    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


def upload_to(instance, filename):
    return 'tune_app/{filename}'.format(filename=filename)

class Album(models.Model):
    name = models.CharField(max_length=300)

    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name="albums")
    genre = models.ManyToManyField(Genre, related_name="album_list", blank=True)
    release = models.DateField(default=date.today)
    image = models.ImageField(
        _("Image"), upload_to=upload_to, default="tune_app/IMG_1717.jpg")
    avg_rating = models.FloatField(default=0)

    

class Song(models.Model):
    title = models.CharField(max_length=300)

    duration = models.CharField(max_length=200)

    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="songs")

    def __str__(self):
        return self.title




class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)

    genre = models.ManyToManyField(
        Genre, related_name="post_list", blank=True)
    artist = models.ForeignKey(
            Artist, on_delete=models.CASCADE, related_name="artists")

    album = models.ForeignKey(
            Album, on_delete=models.CASCADE, related_name="posts")

    published = models.DateTimeField(default=timezone.now)

    content = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')

    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="likes", blank=True)
        
    status = models.CharField(
        max_length=10, choices=options, default='published')
    
    rating = models.SmallIntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    objects = models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title