from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# accounts
from accounts.models import UserFavoriteMovie
from accounts.models import UserSimilarMovie

# articles
from articles.models import ReviewArticle
from articles.models import TalkArticle
from articles.models import ReviewComment
from articles.models import TalkComment

# movies
from movies.models import Movie
from movies.models import Genre
from movies.models import MovieGenre
from movies.models import UserScore
from movies.models import MovieComment





# Register your models here.
admin.site.register(User, UserAdmin)

# accounts
admin.site.register(UserFavoriteMovie)
admin.site.register(UserSimilarMovie)

# articles
admin.site.register(ReviewArticle)
admin.site.register(TalkArticle)
admin.site.register(ReviewComment)
admin.site.register(TalkComment)

# movies
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(MovieGenre)
admin.site.register(UserScore)
admin.site.register(MovieComment)

