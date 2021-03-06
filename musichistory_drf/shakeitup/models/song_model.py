from django.db import models
from . import artist_model

class Song(models.Model):
    '''
    Song Model contains the essential fields and behaviors of Song Data.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Zoe LeBlanc
    '''
    featured_artist = models.ForeignKey(artist_model.Artist, related_name="+", null=True, on_delete=models.CASCADE)
    collaborating_artist = models.ForeignKey(artist_model.Artist, related_name="+", null=True, on_delete=models.CASCADE)
    composing_artist = models.ForeignKey(artist_model.Artist, related_name="+", null=True, on_delete=models.CASCADE)
    songwriter_artist = models.ForeignKey(artist_model.Artist, related_name="+", null=True, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100, blank=False)
    date_released = models.DateField(null=True)
    song_length = models.DurationField(null=True)
    danceability = models.DecimalField(decimal_places=10, max_digits=20)

    class Meta:
        app_label = "shakeitup"

    def __str__(self):
        return '%s' % (self.song_title)