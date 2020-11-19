from django.db import models
from django.conf import settings

# Create your models here.
class ReviewArticle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_review')
    unlike = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='unlike_review')

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField()
    

    class Rank(models.IntegerChoices):
        BEST = 5
        GOOD = 4
        NORMAL = 3
        BAD = 2
        WORST = 1

    rank = models.IntegerField(choices=Rank.choices)

    def __str__(self):
        return self.title


class TalkArticle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField()
    
    def __str__(self):
        return self.title


class CommunityComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_article = models.ForeignKey(ReviewArticle, on_delete=models.CASCADE)
    talk_article = models.ForeignKey(TalkArticle, on_delete=models.CASCADE)
    # 대댓글 기능 구현
    
    content = models.CharField(max_length=100) 

    def __str__(self):
        return self.content


