from django.db import models

class Album(models.Model):
    album_title = models.CharField(max_length=100, blank=False)
    date_released = models.DateField()

    def __str__(self):
        return '%s' % (self.album_title)