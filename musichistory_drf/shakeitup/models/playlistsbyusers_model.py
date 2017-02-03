from django.db import models
from django.contrib.auth.models import User
from . import playlist_model

class Playlist_By_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_playlists")
    playlist = models.ForeignKey(playlist_model.Playlist, null=True, on_delete=models.CASCADE, related_name="user_playlists")

    class Meta:
        app_label = "shakeitup"

    def __str__(self):
        return '%s' % (self.id)