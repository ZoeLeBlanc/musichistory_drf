from rest_framework import viewsets
from shakeitup.serializers import *
from shakeitup.models import *

class SongByGenreViewSet(viewsets.ModelViewSet):
    ''' The SongByGenreViewSet class is a view that lists out all songs' genres.

    Author: Zoe LeBlanc
    '''
    queryset = songsbygenres_model.Song_By_Genre.objects.all()
    serializer_class = song_serializer.SongByGenreSerializer

class SongOnAlbumViewSet(viewsets.ModelViewSet):
    ''' The SongOnAlbumViewSet class is a view that lists out all songs' albums.

    Author: Zoe LeBlanc
    '''
    queryset = songsonalbums_model.Song_On_Album.objects.all()
    serializer_class = song_serializer.SongOnAlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    ''' The SongViewSet class is a view that lists out all songs and each song's details.

    Author: Zoe LeBlanc
    '''
    queryset = song_model.Song.objects.all()
    serializer_class = song_serializer.SongSerializer