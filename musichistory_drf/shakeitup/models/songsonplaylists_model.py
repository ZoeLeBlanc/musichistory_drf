from django.db import models
from . import song_model, playlist_model

class Song_On_Playlist(models.Model):
    '''
    Song_On_Playlist Model contains the essential fields and behaviors of Song_On_Playlist Data.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Zoe LeBlanc
    '''
    song = models.ForeignKey(song_model.Song, null=True, on_delete=models.CASCADE, related_name="playlist_songs")
    playlist = models.ForeignKey(playlist_model.Playlist, null=True, on_delete=models.CASCADE, related_name="playlist_songs")

    class Meta:
        app_label = "shakeitup"
        
    def __str__(self):
        return '%s' % (self.id)