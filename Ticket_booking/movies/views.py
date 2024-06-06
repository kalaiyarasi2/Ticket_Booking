from django.shortcuts import render

from rest_framework import viewsets
from .models import Movies_details,MovieIDChoices
from .serializers import Movie_detailsserializer ,MovieIDChoicesserializer

class Movies_detailsviewsset(viewsets.ModelViewSet):
    queryset= Movies_details.objects.all()
    serializer_class=Movie_detailsserializer
    
class MovieIDChoiceviewsset(viewsets.ModelViewSet):
    queryset= MovieIDChoices.objects.all()
    serializer_class=MovieIDChoicesserializer