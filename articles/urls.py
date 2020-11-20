from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # review
    path('review/', views.review_index, name="review_index"),
    path('review/create/', views.review_create, name='review_create'),
    path('review/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('review/<int:review_pk>/update/', views.review_update, name='review_update'),
    path('review/<int:review_pk>/delete/', views.review_delete, name='review_delete'),
    path('review/<int:review_pk>/comments/', views.review_create_comment, name='review_create_comment'),
    path('review/<int:review_pk>/comments/<int:comment_pk>/', views.review_delete_comment, name='review_delete_comment'),
    path('review/<int:review_pk>/like/', views.like, name='like'),
    path('review/<int:review_pk>/unlike/', views.unlike, name='unlike'),

    # talk
    path('talk/', views.talk_index, name="talk_index"),
    path('talk/create/', views.talk_create, name='talk_create'),
    path('talk/<int:talk_pk>/', views.talk_detail, name='talk_detail'),
    path('talk/<int:talk_pk>/update/', views.talk_update, name='talk_update'),
    path('talk/<int:talk_pk>/delete/', views.talk_delete, name='talk_delete'),
    path('talk/<int:talk_pk>/comments/', views.talk_create_comment, name='talk_create_comment'),
    path('talk/<int:talk_pk>/comments/<int:comment_pk>/', views.talk_delete_comment, name='talk_delete_comment'),
]