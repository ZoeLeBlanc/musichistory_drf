from django.db import models
from . import album_model, artist_model

class Artist_On_Album(models.Model):
    artist = models.ForeignKey(artist_model.Artist, null=True, on_delete=models.CASCADE, related_name="album_artists")
    album = models.ForeignKey(album_model.Album, null=True, on_delete=models.CASCADE, related_name="album_artists")

    def __str__(self):
        return '%s' % (self.id)