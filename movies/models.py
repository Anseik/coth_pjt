from django.db import models

# Create your models here.
class Movie(models.Model):
    genres = models.CharField(max_length=200)
    original_title = models.TextField()
    overview = models.TextField()
    popularity = models.IntegerField()
    poster_path = models.TextField()
    release_date = models.CharField(max_length=200)
    runtime = models.IntegerField()
    title = models.TextField()
    video = models.BooleanField()
    vote_average = models.IntegerField()
    vote_count = models.IntegerField()
    rank_average = models.IntegerField()
    
    class Rank(models.IntegerChoices):
        BEST = 5
        GOOD = 4
        NORMAL = 3
        BAD = 2
        WORST = 1

    rank = models.IntegerField(choices=Rank.choices)


class MovieComment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    
    