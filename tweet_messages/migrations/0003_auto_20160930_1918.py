# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet_messages', '0002_auto_20160927_1834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweetmessage',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='tweetmessage',
            name='tweet_messages',
            field=models.CharField(max_length=140),
        ),
    ]
