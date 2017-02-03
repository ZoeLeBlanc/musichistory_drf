from rest_framework import serializers
from shakeitup.models import *

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = genre_model.Genre
        fields = '__all__'