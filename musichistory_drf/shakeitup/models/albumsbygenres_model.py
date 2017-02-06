from django.db import models
from . import album_model, genre_model

class Album_By_Genre(models.Model):
    '''
    Album_By_Genre Model contains the essential fields and behaviors of Album_By_Genre Data.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Zoe LeBlanc
    '''
    genre = models.ForeignKey(genre_model.Genre, null=True, on_delete=models.CASCADE, related_name="album_genres")
    album = models.ForeignKey(album_model.Album, null=True, on_delete=models.CASCADE, related_name="album_genres")

    def __str__(self):
        return '%s' % (self.id)