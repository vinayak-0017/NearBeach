# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-26 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0004_api_access'),
    ]

    operations = [
        migrations.AddField(
            model_name='api_access',
            name='domain_limiter',
            field=models.URLField(default='localhost:8000;'),
            preserve_default=False,
        ),
    ]
