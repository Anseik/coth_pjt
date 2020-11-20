from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('savedata/', views.savedata, name="savedata"),
    path('deletedata/', views.deletedata, name="deletedata"),
    path('', views.index, name="index"),
]
