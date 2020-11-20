from django import forms
from .models import ReviewArticle, ReviewComment, TalkArticle, TalkComment


class ReviewArticleForm(forms.ModelForm):

    class Meta:
        model = ReviewArticle
        fields = ['title', 'content', 'image', 'rank',]


class ReviewCommentForm(forms.ModelForm):

    class Meta:
        model = ReviewComment
        fields = ['content',]


class TalkArticleForm(forms.ModelForm):

    class Meta:
        model = TalkArticle
        fields = ['title', 'content', 'image',]


class TalkCommentForm(forms.ModelForm):

    class Meta:
        model = TalkComment
        fields = ['content',]
