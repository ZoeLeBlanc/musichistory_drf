from rest_framework import viewsets
from shakeitup.serializers import *
from shakeitup.models import *


class GenreViewSet(viewsets.ModelViewSet):
    ''' The GenreViewSet class is a view that lists out all genres and each genre's details.

    Author: Zoe LeBlanc
    '''
    queryset = genre_model.Genre.objects.all()
    serializer_class = genre_serializer.GenreSerializer