from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from datetime import datetime
from django.http import HttpResponse

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
    profile_pic = models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse('tweet_messages:user_page', kwargs={'id': self.pk})

class Promo(models.Model):
    user = models.OneToOneField(User)
    promo_code = CharField(max_length=10)

    def __str__(self):
        return self.promo_code