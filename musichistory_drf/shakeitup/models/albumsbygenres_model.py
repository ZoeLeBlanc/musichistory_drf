from django.db import models
from . import album_model, genre_model


class Album_By_Genre(models.Model):
    album = models.ForeignKey(album_model.Album, null=True, on_delete=models.CASCADE, related_name="album_genres")
    genre = models.ForeignKey(genre_model.Genre, null=True, on_delete=models.CASCADE, related_name="album_genres")

    def __str__(self):
        return '%s' % (self.id)