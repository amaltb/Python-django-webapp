from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class Album(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    artist = models.CharField(max_length=50)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=50)
    album_logo = models.FileField()
    is_favourite = models.BooleanField(default=False)

# This is to return to detail page after adding the form data to database.
# since detail page needs the primary_key of the added item,
# Passing primary_key here.
    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100)
    audio_file = models.FileField(default='')
    file_type = models.CharField(max_length=100, default='')
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
