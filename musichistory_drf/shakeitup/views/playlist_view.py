from django.contrib.auth.models import User
from rest_framework import viewsets
from shakeitup.serializers import *
from shakeitup.models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class UserViewSet(viewsets.ModelViewSet):
    ''' The UserViewSet class is a view that lists out all users and each user's details.

    Author: Zoe LeBlanc
    '''
    queryset = User.objects.all()
    serializer_class = playlist_serializer.UserSerializer

class SongOnPlaylistViewSet(viewsets.ModelViewSet):
    ''' The SongOnPlaylistViewSet class is a view that lists out all playlists' songs.

    Author: Zoe LeBlanc
    '''
    queryset = songsonplaylists_model.Song_On_Playlist.objects.all()
    serializer_class = playlist_serializer.SongOnPlaylistSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    ''' The PlaylistViewSet class is a view that lists out all playlists and each playlist's details.

    Author: Zoe LeBlanc
    '''
    queryset = playlist_model.Playlist.objects.all()
    serializer_class = playlist_serializer.PlaylistSerializer