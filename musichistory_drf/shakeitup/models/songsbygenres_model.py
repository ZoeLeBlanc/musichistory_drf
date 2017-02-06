from django.db import models
from . import song_model, genre_model

class Song_By_Genre(models.Model):
    '''
    Song_By_Genre Model contains the essential fields and behaviors of Song_By_Genre Data.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Zoe LeBlanc
    '''
    song = models.ForeignKey(song_model.Song, null=True, on_delete=models.CASCADE, related_name="song_genres")
    genre = models.ForeignKey(genre_model.Genre, null=True, on_delete=models.CASCADE, related_name="song_genres")

    class Meta:
        app_label = "shakeitup"

    def __str__(self):
        return '%s' % (self.id)