from rest_framework import serializers
from .models import Movies_details

class Movie_detailsserializer(serializers.ModelSerializer):
    class  Meta:
        model='Movie_details'
        fields='_all_'
        
class MovieIDChoicesserializer(serializers.ModelSerializer):
    class Meta:
        model='MovieIDChoice'
        fields='all'