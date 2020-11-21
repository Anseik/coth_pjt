from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/update/', views.update, name='update'),
    path('<int:user_pk>/password/', views.password_change, name='password_change'),
    path('<int:user_pk>/delete/', views.delete, name='delete'),
    path('<int:user_pk>/', views.profile, name='profile'),
    path('follow/<int:user_pk>/', views.follow, name='follow'),
]
