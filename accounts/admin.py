from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from articles.models import ReviewArticle
from articles.models import TalkArticle
from articles.models import ReviewComment
from articles.models import TalkComment

from movies.models import Movie
from movies.models import MovieComment


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(ReviewArticle)
admin.site.register(TalkArticle)
admin.site.register(ReviewComment)
admin.site.register(TalkComment)
admin.site.register(Movie)
admin.site.register(MovieComment)

