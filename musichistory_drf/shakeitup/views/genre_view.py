from rest_framework import viewsets
from shakeitup.serializers import *
from shakeitup.models import *


class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = genre_model.Genre.objects.all()
    serializer_class = genre_serializer.GenreSerializer