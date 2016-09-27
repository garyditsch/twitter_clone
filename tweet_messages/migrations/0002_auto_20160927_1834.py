# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet_messages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='tweetmessage',
            name='hashtag',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
