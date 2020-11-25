from django import forms
from .models import ReviewArticle, ReviewComment, TalkArticle, TalkComment
from django_summernote.widgets import SummernoteWidget



class ReviewArticleForm(forms.ModelForm):

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
