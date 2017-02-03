from rest_framework import viewsets
from shakeitup.serializers import *
from shakeitup.models import *

class SongByGenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = songsbygenres_model.Song_By_Genre.objects.all()
    serializer_class = song_serializer.SongByGenreSerializer

class SongOnAlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = songsonalbums_model.Song_On_Album.objects.all()
    serializer_class = song_serializer.SongOnAlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = song_model.Song.objects.all()
    serializer_class = song_serializer.SongSerializer