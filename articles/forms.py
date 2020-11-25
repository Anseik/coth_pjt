from django import forms
from .models import ReviewArticle, ReviewComment, TalkArticle, TalkComment
from django_summernote.widgets import SummernoteWidget



class ReviewArticleForm(forms.ModelForm):
    RANK_CHOICES = (
        (5, '최고에요'),
        (4, '재밌어요'),
        (3, '킬링 타임용'),
        (2, '재미없어요'),
        (1, '최악이에요')
    )    

    rank = forms.ChoiceField(choices=RANK_CHOICES, widget=forms.RadioSelect(), label='평점')

    class Meta:
        model = ReviewArticle
        fields = ['title', 'content', 'rank',]
        widgets = {
            'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
        }        


class ReviewCommentForm(forms.ModelForm):

    class Meta:
        model = ReviewComment
        fields = ['content',]


class TalkArticleForm(forms.ModelForm):

    class Meta:
        model = TalkArticle
        fields = ['title', 'content',]
        widgets = {
            'content': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
        }        


class TalkCommentForm(forms.ModelForm):

    class Meta:
        model = TalkComment
        fields = ['content',]
