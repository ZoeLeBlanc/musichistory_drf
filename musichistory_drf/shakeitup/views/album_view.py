from rest_framework import viewsets
from shakeitup.serializers import *
from shakeitup.models import *

class AlbumByGenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = albumsbygenres_model.Album_By_Genre.objects.all()
    serializer_class = album_serializer.AlbumByGenreSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = album_model.Album.objects.all()
    serializer_class = album_serializer.AlbumSerializer