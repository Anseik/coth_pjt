from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserChangeForm(UserChangeForm):
    selfpr = forms.CharField(
        label = "자기소개",
        widget=forms.TextInput(attrs={
            'class': 'my-content form-control',
            'placeholder': '자기소개를 입력해주세요',
            'maxlength' : 300,
        })
    )

    class Meta:
        model = get_user_model()
        fields = ['email', 'nickname', 'image', 'selfpr']

class CustomUserCreationForm(UserCreationForm):
    selfpr = forms.CharField(
        label = "자기소개",
        widget=forms.TextInput(attrs={
            'class': 'my-content form-control',
            'placeholder': '자기소개를 입력해주세요',
            'maxlength' : 300,
        })
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email', 'nickname', 'image', 'selfpr')

