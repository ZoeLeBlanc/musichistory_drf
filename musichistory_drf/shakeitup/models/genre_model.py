from django.db import models

class Genre(models.Model):
    '''
    Genre Model contains the essential fields and behaviors of Genre Data.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Zoe LeBlanc
    '''
    genre_type = models.CharField(max_length=100, blank=False)

    class Meta:
        app_label = "shakeitup"
        
    def __str__(self):
        return '%s' % (self.genre_type)