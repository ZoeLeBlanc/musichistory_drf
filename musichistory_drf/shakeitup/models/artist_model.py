from django.db import models

class Artist(models.Model):
    '''
    Artist Model contains the essential fields and behaviors of Artist Data.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Zoe LeBlanc
    '''
    stage_name = models.CharField(max_length=100, blank=False)
    birth_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return '%s' % (self.stage_name)