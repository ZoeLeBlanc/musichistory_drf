from django.db import models
from . import song_model, genre_model

class Song_By_Genre(models.Model):
    song = models.ForeignKey(song_model.Song, null=True, on_delete=models.CASCADE, related_name="song_genres")
    genre = models.ForeignKey(genre_model.Genre, null=True, on_delete=models.CASCADE, related_name="song_genres")

    class Meta:
        app_label = "shakeitup"

    def __str__(self):
        return '%s' % (self.id)