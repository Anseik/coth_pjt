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

    class Prefer(models.IntegerChoices):
        액션 = 28
        모험 = 12
        애니메이션 = 16
        코미디 = 35
        범죄 = 80
        다큐멘터리 = 99
        드라마 = 18
        가족 = 10751
        판타지 = 14
        역사 = 36
        공포 = 27
        음악 = 10402
        미스터리 = 9648
        로맨스 = 10749
        SF = 878
        TV영화 = 10770
        스릴러 = 53
        전쟁 = 10752
        서부 = 37

    genre_prefer1 = models.IntegerField(choices=Prefer.choices)
    genre_prefer2 = models.IntegerField(choices=Prefer.choices)
    genre_prefer3 = models.IntegerField(choices=Prefer.choices)    


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



    


   


    