from django import forms
from .models import Image,Comment, Profile

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'post_date', 'likes', 'comments']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('created_on', 'user')

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)