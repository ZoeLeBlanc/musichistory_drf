from rest_framework import viewsets
from shakeitup.serializers import *
from shakeitup.models import *


class ArtistOnAlbumViewSet(viewsets.ModelViewSet):
    ''' The ArtistOnAlbumViewSet class is a view that lists out all artists' albums.

    Author: Zoe LeBlanc
    '''
    queryset = artistsonalbums_model.Artist_On_Album.objects.all()
    serializer_class = artist_serializer.ArtistOnAlbumSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    ''' The ArtistViewSet class is a view that lists out all artists and each artist's details.

    Author: Zoe LeBlanc
    '''
    queryset = artist_model.Artist.objects.all()
    serializer_class = artist_serializer.ArtistSerializer