from django.db import models
class MovieIDChoices(models.IntegerChoices):
    ACTION=1
    COMEDY=2
    DRAMA=3
    HORROR=4

class Movies_details(models.Model):
    movie_id=models.IntegerField(choices = MovieIDChoices.choices)
    title=models.CharField(max_length=200)
    genre=models.CharField(max_length=100)
    duration=models.DurationField()
    direction=models.CharField(max_length=100)
    cast=models.TextField()
    synopsis=models.TextField()
    release_date=models.DateField()
    language=models.CharField(max_length=100)
    poster_url=models.URLField(max_length=200)
    trailer_url=models.URLField(max_length=200)
    
    def __str__(self):
        return self.title



