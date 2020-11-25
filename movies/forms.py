from django import forms
from .models import MovieComment, UserScore

class MovieCommentForm(forms.ModelForm):

    class Meta:
        model = MovieComment
        fields = ['content',]


class UserScoreForm(forms.ModelForm):
    SCORE_CHOICES = (
        (5, '최고에요 꼭 보세요'),
        (4, '재밌어요 추천'),
        (3, '킬링 타임용이에요'),
        (2, '재미없어요 비추천'),
        (1, '최악이에요 절대 보지마세요')
    )

    score = forms.ChoiceField(choices=SCORE_CHOICES, widget=forms.RadioSelect(), label='평점 주기')

    class Meta:
        model = UserScore
        fields = ['score']