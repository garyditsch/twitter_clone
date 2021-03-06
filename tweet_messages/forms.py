from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 
from phonenumber_field.modelfields import PhoneNumberField
from django import forms
from .models import TweetMessage, Promo, Profile
from . import views


class TweetMessageForm(forms.ModelForm):
    tweet_messages = forms.CharField(max_length=140)
    
    class Meta:
        model = TweetMessage
        fields = ('tweet_messages',)


class LoginForm(AuthenticationForm):
    pass

class PromoForm(forms.ModelForm):
    promo_code = forms.CharField(max_length=10)

    class Meta:
        model = Promo
        fields = ('promo_code',)


class ProfileForm(forms.ModelForm):
    phone_number = PhoneNumberField()
    bio = forms.CharField(max_length=200)

    class Meta:
        model = Profile
        fields = ('bio', 'phone_number')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password', 'password2',)


    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']