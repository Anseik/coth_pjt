from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

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