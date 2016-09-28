from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 
from django import forms
from .models import TweetMessage, Profile
from . import views


class TweetMessageForm(forms.ModelForm):
    tweet_messages = forms.CharField(max_length=140)
    
    class Meta:
        model = TweetMessage
        fields = ('tweet_messages',)


class LoginForm(AuthenticationForm):
    pass

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')

        return cd['password2']