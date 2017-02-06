from django.db import models
from . import album_model, song_model

class Song_On_Album(models.Model):
    '''
    Song_On_Album Model contains the essential fields and behaviors of Song_On_Album Data.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Zoe LeBlanc
    '''
    album = models.ForeignKey(album_model.Album, null=True, on_delete=models.CASCADE, related_name="album_songs")
    song = models.ForeignKey(song_model.Song, null=True, on_delete=models.CASCADE, related_name="album_songs")

    def __str__(self):
        return '%s' % (self.id)