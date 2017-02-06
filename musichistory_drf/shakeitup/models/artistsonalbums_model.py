from django.db import models
from . import album_model, artist_model

class Artist_On_Album(models.Model):
    '''
    Artist_On_Album Model contains the essential fields and behaviors of Artist_On_Album Data.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Zoe LeBlanc
    '''
    artist = models.ForeignKey(artist_model.Artist, null=True, on_delete=models.CASCADE, related_name="artist_albums")
    album = models.ForeignKey(album_model.Album, null=True, on_delete=models.CASCADE, related_name="artist_albums")

    def __str__(self):
        return '%s' % (self.id)