from django.contrib.auth.models import User
from rest_framework import serializers
from shakeitup.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    ''' The UserSerializer class translates the User model into other formats, in this case JSON by default. This serializer returns specific fields.

    Author: Zoe LeBlanc
    '''
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class SongOnPlaylistSerializer(serializers.HyperlinkedModelSerializer):
    ''' The SongOnPlaylistSerializer class translates the Song_On_Playlist model into other formats, in this case JSON by default. This serializer returns all fields.

    Author: Zoe LeBlanc
    '''
    class Meta:
        model = songsonplaylists_model.Song_On_Playlist
        fields = '__all__'

class PlaylistSongsSerializer(serializers.HyperlinkedModelSerializer):
    ''' The PlaylistSongsSerializer class translates the Song_On_Playlist model into other formats, in this case JSON by default. This serializer returns specific fields.

    Author: Zoe LeBlanc
    '''
    class Meta:
        model = songsonplaylists_model.Song_On_Playlist
        fields = ('url', 'song')
        depth = 1

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    ''' The PlaylistSerializer class translates the Playlist model into other formats, in this case JSON by default. This serializer returns specific fields.

    Author: Zoe LeBlanc
    '''
    playlist_songs = PlaylistSongsSerializer(many=True, read_only=True)
    class Meta:
        model = playlist_model.Playlist
        fields = ('url', 'playlist_name', 'date_created', 'date_updated', 'playlist_songs', 'user')
        depth = 1