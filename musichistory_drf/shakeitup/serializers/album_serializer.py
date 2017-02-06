from rest_framework import serializers
from shakeitup.models import *

class AlbumByGenreSerializer(serializers.HyperlinkedModelSerializer):
    ''' The AlbumByGenreSerializer class translates the Album_By_Genre model into other formats, in this case JSON by default. This serializer returns all fields.

    Author: Zoe LeBlanc
    '''
    class Meta:
        model = albumsbygenres_model.Album_By_Genre
        fields = '__all__'

class AlbumGenresSerializer(serializers.HyperlinkedModelSerializer):
    ''' The AlbumGenresSerializer class translates the Album_By_Genre model into other formats, in this case JSON by default. This serializer returns specific fields.

    Author: Zoe LeBlanc
    '''
    class Meta:
        model = albumsbygenres_model.Album_By_Genre
        fields = ('url', 'genre')
        depth = 1

class AlbumArtistsSerializer(serializers.HyperlinkedModelSerializer):
    ''' The AlbumArtistsSerializer class translates the Artist_On_Album model into other formats, in this case JSON by default. This serializer returns specific fields.

    Author: Zoe LeBlanc
    '''
    class Meta:
        model = artistsonalbums_model.Artist_On_Album
        fields = ('url', 'artist')
        depth = 1

class AlbumSongsSerializer(serializers.HyperlinkedModelSerializer):
    ''' The AlbumSongsSerializer class translates the Song_On_Album model into other formats, in this case JSON by default. This serializer returns specific fields.

    Author: Zoe LeBlanc
    '''
    class Meta:
        model = songsonalbums_model.Song_On_Album
        fields = ('url', 'song')
        depth = 1

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    ''' The AlbumSerializer class translates the Album model into other formats, in this case JSON by default. 

    Author: Zoe LeBlanc
    '''
    album_genres = AlbumGenresSerializer(many=True, read_only=True)
    artist_albums = AlbumArtistsSerializer(many=True, read_only=True)
    album_songs = AlbumSongsSerializer(many=True, read_only=True)
    class Meta:
        model = album_model.Album
        fields = ('url','album_title', 'date_released', 'album_genres', 'artist_albums', 'album_songs')
        depth = 2