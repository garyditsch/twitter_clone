from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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

class UserRegistrationForm(UserCreationForm):
    pass