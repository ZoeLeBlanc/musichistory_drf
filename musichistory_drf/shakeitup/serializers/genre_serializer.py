from rest_framework import serializers
from shakeitup.models import *

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    ''' The GenreSerializer class translates the Genre model into other formats, in this case JSON by default. This serializer returns all fields.

    Author: Zoe LeBlanc
    '''
    class Meta:
        model = genre_model.Genre
        fields = '__all__'