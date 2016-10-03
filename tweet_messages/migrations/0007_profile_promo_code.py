# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet_messages', '0006_remove_promo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='promo_code',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
