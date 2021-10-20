from django import forms
from instagram import views
from django.contrib.auth.models import User
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

class SignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), max_length=30, required=True,)
    email = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), max_length=100, required=True,)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-medium'}),)
    # confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input is-medium'}), required=True, label="Confirm your password.")

    class Meta:

        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append('ForbiddenUsers')
        self.fields['username'].validators.append('InvalidUser')
        self.fields['username'].validators.append('UniqueUser')
        self.fields['email'].validators.append('UniqueEmail')