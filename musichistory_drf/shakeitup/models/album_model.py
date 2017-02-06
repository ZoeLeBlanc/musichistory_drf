from django.db import models

class Album(models.Model):
    '''
    Album Model contains the essential fields and behaviors of Album Data.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Zoe LeBlanc
    '''
    album_title = models.CharField(max_length=100, blank=False)
    date_released = models.DateField()

    def __str__(self):
        return '%s' % (self.album_title)