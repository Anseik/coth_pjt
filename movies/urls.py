from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # 관리자
    path('savedata/', views.savedata, name="savedata"),
    path('deletedata/', views.deletedata, name="deletedata"),

    # 사용자 
    path('', views.index, name="index"),
    path('detail/<int:movie_pk>/', views.detail, name="detail"),
    path('detail/<int:movie_pk>/comments/', views.movie_create_comment, name='movie_create_comment'),
    path('detail/<int:movie_pk>/comments/<int:comment_pk>/', views.movie_delete_comment, name='movie_delete_comment'),

    # 추천 알고리즘
    path('saveuserscore/<int:movie_pk>/', views.save_user_score, name="save_user_score"),
    path('deluserscore/<int:movie_pk>/', views.delete_user_score, name="delete_user_score"),
    path('similar/<int:movie_pk>/', views.similar, name="similar"),
]
