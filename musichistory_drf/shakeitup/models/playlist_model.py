from django.db import models
# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Playlist(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=100, blank=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        app_label = "shakeitup"

    # @receiver(post_save, sender=User)
    # def create_user_playlist(sender, instance, created, **kwargs):
    #     if created:
    #         Playlist.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_playlist(sender, instance, **kwargs):
    #     instance.playlist.save()

    def __str__(self):
        return '%s' % (self.playlist_name)