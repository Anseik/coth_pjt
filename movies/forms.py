from django import forms
from .models import MovieComment, UserScore

class MovieCommentForm(forms.ModelForm):

    class Meta:
        model = MovieComment
        fields = ['content',]


class UserScoreForm(forms.ModelForm):

    class Meta:
        model = UserScore
        fields = ['score']