from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # 관리자
    path('savedata/', views.savedata, name="savedata"),
    path('deletedata/', views.deletedata, name="deletedata"),
    path('savegenres/', views.save_genres, name="save_genres"),
    path('deletegenres/', views.delete_genres, name="delete_genres"),

    # 사용자 
    path('', views.index, name="index"),
    path('detail/<int:movie_pk>/', views.detail, name="detail"),
    path('detail/<int:movie_pk>/comments/', views.movie_create_comment, name='movie_create_comment'),
    path('detail/<int:movie_pk>/comments/<int:comment_pk>/', views.movie_delete_comment, name='movie_delete_comment'),
    path('newmovies/', views.new_movies, name='new_movies'),
    path('search/', views.search, name='search'),
    path('mytype/', views.mytype_movie, name='mytype_movie'),
    path('mytypedetail/<int:movie_pk>/', views.mytype_detail, name='mytype_detail'),


    # 추천 알고리즘
    path('saveuserscore/<int:movie_pk>/', views.save_user_score, name="save_user_score"),
    path('deluserscore/<int:movie_pk>/', views.delete_user_score, name="delete_user_score"),
    # path('similar/<int:movie_pk>/', views.similar, name="similar"),

    # ajax 요청
    path('<int:movie_pk>/dibs/', views.dibs_movie, name="dibs_movie"),
    path('<int:user_pk>/mydibs/', views.mydibs_movie, name="mydibs_movie"),
]
