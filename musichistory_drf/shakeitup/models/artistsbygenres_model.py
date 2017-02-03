from django.db import models
from . import artist_model, genre_model

class Artist_By_Genre(models.Model):
    artist = models.ForeignKey(artist_model.Artist, null=True, on_delete=models.CASCADE, related_name="artist_genres")
    genre = models.ForeignKey(genre_model.Genre, null=True, on_delete=models.CASCADE, related_name="artist_genres")

    def __str__(self):
        return '%s' % (self.id)