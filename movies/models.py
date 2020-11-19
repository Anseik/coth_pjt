from django.db import models

# Create your models here.
class Movie(models.Model):
    popularity = models.IntegerField()
    vote_count = models.IntegerField()
    video = models.BooleanField()
    poster_path = models.TextField()
    original_language = models.TextField()
    original_title = models.TextField()
    genre_ids = models.TextField()
    title = models.TextField()
    vote_average = models.IntegerField()
    overview = models.TextField()
    release_date = models.TextField()


class MovieInfo(models.Model):
    genres = models.TextField()
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
    
    