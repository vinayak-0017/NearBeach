# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-31 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0006_auto_20180331_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission_set',
            name='bug',
            field=models.IntegerField(choices=[(0, 'No Permission'), (1, 'Read Only'), (2, 'Edit Only'), (3, 'Add and Edit'), (4, 'Full Permission')], default=0),
        ),
        migrations.AddField(
            model_name='permission_set',
            name='bug_client',
            field=models.IntegerField(choices=[(0, 'No Permission'), (1, 'Read Only'), (2, 'Edit Only'), (3, 'Add and Edit'), (4, 'Full Permission')], default=0),
        ),
    ]
