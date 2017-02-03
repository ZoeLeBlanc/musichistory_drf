from rest_framework import serializers
from shakeitup.models import *

class AlbumByGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = albumsbygenres_model.Album_By_Genre
        fields = '__all__'

class AlbumGenresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = albumsbygenres_model.Album_By_Genre
        fields = ('url', 'genre')
        depth = 1

class AlbumArtistsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = artistsonalbums_model.Artist_On_Album
        fields = ('url', 'artist')
        depth = 1

class AlbumSongsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = songsonalbums_model.Song_On_Album
        fields = ('url', 'song')
        depth = 1

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    album_genres = AlbumGenresSerializer(many=True, read_only=True)
    album_artists = AlbumArtistsSerializer(many=True, read_only=True)
    album_songs = AlbumSongsSerializer(many=True, read_only=True)
    class Meta:
        model = album_model.Album
        fields = ('url','album_title', 'date_released', 'album_genres', 'album_artists', 'album_songs')
        depth = 2