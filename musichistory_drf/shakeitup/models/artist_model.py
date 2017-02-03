from django.db import models

class Artist(models.Model):
    stage_name = models.CharField(max_length=100, blank=False)
    birth_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return '%s' % (self.stage_name)