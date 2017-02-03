from rest_framework import serializers
from shakeitup.models import *

class ArtistByGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = artistsbygenres_model.Artist_By_Genre
        fields = '__all__'

class ArtistOnAlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = artistsonalbums_model.Artist_On_Album
        fields = '__all__'


class ArtistGenresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = artistsbygenres_model.Artist_By_Genre
        fields = ('url', 'genre')
        depth = 1

class ArtistAlbumsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = artistsonalbums_model.Artist_On_Album
        fields = ('url', 'album')
        depth = 1


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    artist_genres = ArtistGenresSerializer(many=True, read_only=True)
    album_artists = ArtistAlbumsSerializer(many=True, read_only=True)
    class Meta:
        model = artist_model.Artist
        fields = ('url', 'stage_name', 'birth_name', 'artist_genres', 'album_artists')
        depth = 2