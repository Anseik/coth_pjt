from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

from django.conf import settings

from movies.models import Movie

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    image = ProcessedImageField(blank=True,
                                processors=[Thumbnail(150, 150)],
                                format='png',
                                options={'quality': 100},
                                upload_to='%Y/%m/%d')
    selfpr = models.CharField(max_length=100)
    nickname = models.CharField(max_length=20)
    dibs_movies = models.ManyToManyField(Movie, related_name='dibs_users', blank=True, null=True)


class UserFavoriteMovie(models.Model):
    popularity = models.IntegerField()
    vote_count = models.IntegerField()
    video = models.BooleanField()
    poster_path = models.TextField()
    movie_id = models.IntegerField()
    original_language = models.TextField()
    original_title = models.TextField()
    genre_ids = models.TextField()
    title = models.TextField()
    vote_average = models.IntegerField()
    overview = models.TextField()
    release_date = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     


class UserSimilarMovie(models.Model):
    popularity = models.IntegerField()
    vote_count = models.IntegerField()
    video = models.BooleanField()
    poster_path = models.TextField()
    movie_id = models.IntegerField()
    original_language = models.TextField()
    original_title = models.TextField()
    genre_ids = models.TextField()
    title = models.TextField()
    vote_average = models.IntegerField()
    overview = models.TextField()
    release_date = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



    


   


    