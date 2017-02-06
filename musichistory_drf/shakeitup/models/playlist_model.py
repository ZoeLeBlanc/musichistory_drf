from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Playlist(models.Model):
    '''
    Playlist Model contains the essential fields and behaviors of Playlist Data.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Zoe LeBlanc
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    playlist_name = models.CharField(max_length=100, blank=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        app_label = "shakeitup"

    def __str__(self):
        return '%s' % (self.playlist_name)