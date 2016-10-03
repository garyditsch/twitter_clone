from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from datetime import datetime
from django.http import HttpResponse
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class TweetMessage(models.Model):
    tweet_messages = models.CharField(max_length=140)
    user = models.ForeignKey(User)
    date = models.DateTimeField('date created', default=datetime.now)
    hashtag = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ['-date']


    def __str__(self):
        return self.tweet_messages

class Profile(models.Model):
    user = models.OneToOneField(User)
    bio = models.CharField(max_length=200, blank=True)
    profile_pic = models.ImageField(blank=True)
    phone_number = PhoneNumberField(blank=True)
    promo_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.user.username
    

class Promo(models.Model):
    promo_code = models.CharField(max_length=10)

    def __str__(self):
        return self.promo_code