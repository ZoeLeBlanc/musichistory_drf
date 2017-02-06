from rest_framework import serializers
from shakeitup.models import *

class ArtistOnAlbumSerializer(serializers.HyperlinkedModelSerializer):
    ''' The ArtistOnAlbumSerializer class translates the Artist_On_Album model into other formats, in this case JSON by default. This serializer returns all values.

    Author: Zoe LeBlanc
    '''
    class Meta:
        model = artistsonalbums_model.Artist_On_Album
        fields = '__all__'

class ArtistAlbumsSerializer(serializers.HyperlinkedModelSerializer):
    ''' The ArtistAlbumsSerializer class translates the Artist_On_Album model into other formats, in this case JSON by default. This serializer returns specific fields.

    Author: Zoe LeBlanc
    '''
    class Meta:
        model = artistsonalbums_model.Artist_On_Album
        fields = ('url', 'album')
        depth = 1


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    ''' The ArtistSerializer class translates the Artist_On_Album model into other formats, in this case JSON by default. 

    Author: Zoe LeBlanc
    '''
    artist_albums = ArtistAlbumsSerializer(many=True, read_only=True)
    class Meta:
        model = artist_model.Artist
        fields = ('url', 'stage_name', 'birth_name', 'artist_albums')
        depth = 2