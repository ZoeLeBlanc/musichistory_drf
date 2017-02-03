from django.contrib.auth.models import User
from rest_framework import serializers
from shakeitup.models import *

class PlaylistByUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = playlistsbyusers_model.Playlist_By_User
        fields = '__all__'

class UserPlaylistsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = playlistsbyusers_model.Playlist_By_User
        fields = ('url', 'playlist')
        depth = 1

class PlaylistUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = playlistsbyusers_model.Playlist_By_User
        fields = ('url', 'user')
        depth = 1

class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_playlists = UserPlaylistsSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups', 'user_playlists')
        depth = 2

class SongOnPlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = songsonplaylists_model.Song_On_Playlist
        fields = '__all__'

class PlaylistSongsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = songsonplaylists_model.Song_On_Playlist
        fields = ('url', 'song')
        depth = 1

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    playlist_songs = PlaylistSongsSerializer(many=True, read_only=True)
    user_playlists = PlaylistUserSerializer(many=True, read_only=True)
    class Meta:
        model = playlist_model.Playlist
        fields = ('url', 'playlist_name', 'date_created', 'date_updated', 'playlist_songs', 'user_playlists')
        depth = 1