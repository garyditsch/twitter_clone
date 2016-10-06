# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet_messages', '0007_profile_promo_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='promo_code',
        ),
    ]
