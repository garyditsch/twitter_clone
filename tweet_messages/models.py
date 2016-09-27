from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class TweetMessage(models.Model):
    tweet_messages = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    date = models.DateTimeField('date created', default=datetime.now)
    hashtag = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.tweet_messages

class Profile(models.Model):
    user = models.OneToOneField(User)
    profile_pic = models.ImageField(blank=True)
