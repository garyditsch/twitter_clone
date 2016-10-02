# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet_messages', '0005_profile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promo',
            name='user',
        ),
    ]
