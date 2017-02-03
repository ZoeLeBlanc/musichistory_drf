from rest_framework import serializers
from shakeitup.models import *

class SongByGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = songsbygenres_model.Song_By_Genre
        fields = '__all__'

class SongGenresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = songsbygenres_model.Song_By_Genre
        fields = ('url', 'genre')
        depth = 1

class SongOnAlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = songsonalbums_model.Song_On_Album
        fields = '__all__'


class AlbumSongsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = songsonalbums_model.Song_On_Album
        fields = ('url', 'album')
        depth = 1


class SongSerializer(serializers.HyperlinkedModelSerializer):
    song_genres = SongGenresSerializer(many=True, read_only=True)
    album_songs = AlbumSongsSerializer(many=True, read_only=True)
    class Meta:
        model = song_model.Song
        fields = ('url', 'featured_artist', 'collaborating_artist', 'composing_artist', 'songwriter_artist', 'song_title', 'song_length', 'danceability', 'song_genres', 'album_songs')
        depth = 2