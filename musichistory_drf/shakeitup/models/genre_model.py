from django.db import models

class Genre(models.Model):
    genre_type = models.CharField(max_length=100, blank=False)

    class Meta:
        app_label = "shakeitup"
        
    def __str__(self):
        return '%s' % (self.genre_type)