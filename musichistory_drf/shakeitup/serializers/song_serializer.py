from rest_framework import serializers
from shakeitup.models import *

class SongByGenreSerializer(serializers.HyperlinkedModelSerializer):
    ''' The SongByGenreSerializer class translates the Song_By_Genre model into other formats, in this case JSON by default. This serializer returns all fields.

    Author: Zoe LeBlanc
    '''
    class Meta:
        model = songsbygenres_model.Song_By_Genre
        fields = '__all__'

class SongGenresSerializer(serializers.HyperlinkedModelSerializer):
    ''' The SongGenresSerializer class translates the Song_By_Genre model into other formats, in this case JSON by default. This serializer returns specific fields.

    Author: Zoe LeBlanc
    '''
    class Meta:
        model = songsbygenres_model.Song_By_Genre
        fields = ('url', 'genre')
        depth = 1

class SongOnAlbumSerializer(serializers.HyperlinkedModelSerializer):
    ''' The SongOnAlbumSerializer class translates the Song_On_Album model into other formats, in this case JSON by default. This serializer returns all fields.

    Author: Zoe LeBlanc
    '''
    class Meta:
        model = songsonalbums_model.Song_On_Album
        fields = '__all__'


class AlbumSongsSerializer(serializers.HyperlinkedModelSerializer):
    ''' The AlbumSongsSerializer class translates the Song_On_Album model into other formats, in this case JSON by default. This serializer returns specific fields.

    Author: Zoe LeBlanc
    '''
    class Meta:
        model = songsonalbums_model.Song_On_Album
        fields = ('url', 'album')
        depth = 1


class SongSerializer(serializers.HyperlinkedModelSerializer):
    ''' The SongSerializer class translates the Song model into other formats, in this case JSON by default. This serializer returns all fields.

    Author: Zoe LeBlanc
    '''
    song_genres = SongGenresSerializer(many=True, read_only=True)
    album_songs = AlbumSongsSerializer(many=True, read_only=True)
    class Meta:
        model = song_model.Song
        fields = ('url', 'featured_artist', 'collaborating_artist', 'composing_artist', 'songwriter_artist', 'song_title', 'song_length', 'danceability', 'song_genres', 'album_songs')
        depth = 2