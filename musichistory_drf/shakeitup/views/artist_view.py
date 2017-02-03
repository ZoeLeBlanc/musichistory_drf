from rest_framework import viewsets
from shakeitup.serializers import *
from shakeitup.models import *

class ArtistByGenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = artistsbygenres_model.Artist_By_Genre.objects.all()
    serializer_class = artist_serializer.ArtistByGenreSerializer

class ArtistOnAlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = artistsonalbums_model.Artist_On_Album.objects.all()
    serializer_class = artist_serializer.ArtistOnAlbumSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = artist_model.Artist.objects.all()
    serializer_class = artist_serializer.ArtistSerializer