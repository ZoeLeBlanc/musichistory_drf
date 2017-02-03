from django.contrib.auth.models import User
from rest_framework import viewsets
from shakeitup.serializers import *
from shakeitup.models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = playlist_serializer.UserSerializer

class PlaylistByUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = playlistsbyusers_model.Playlist_By_User.objects.all()
    serializer_class = playlist_serializer.PlaylistByUserSerializer

class SongOnPlaylistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = songsonplaylists_model.Song_On_Playlist.objects.all()
    serializer_class = playlist_serializer.SongOnPlaylistSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = playlist_model.Playlist.objects.all()
    serializer_class = playlist_serializer.PlaylistSerializer