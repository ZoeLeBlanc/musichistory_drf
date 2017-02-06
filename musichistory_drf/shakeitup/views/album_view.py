from rest_framework import viewsets
from shakeitup.serializers import *
from shakeitup.models import *

class AlbumByGenreViewSet(viewsets.ModelViewSet):
    ''' The AlbumByGenreViewSet class is a view that lists out all album's genres.

    Author: Zoe LeBlanc
    '''
    queryset = albumsbygenres_model.Album_By_Genre.objects.all()
    serializer_class = album_serializer.AlbumByGenreSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    ''' The AlbumViewSet class is a view that lists out all albums and each album's details.

    Author: Zoe LeBlanc
    '''
    queryset = album_model.Album.objects.all()
    serializer_class = album_serializer.AlbumSerializer