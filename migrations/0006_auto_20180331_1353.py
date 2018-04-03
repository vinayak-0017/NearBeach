# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-31 02:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NearBeach', '0005_api_access_domain_limiter'),
    ]

    operations = [
        migrations.CreateModel(
            name='bug',
            fields=[
                ('bug_id', models.AutoField(primary_key=True, serialize=False)),
                ('bug_code', models.CharField(max_length=255)),
                ('bug_description', models.TextField()),
                ('bug_status', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=5)),
            ],
            options={
                'db_table': 'bug',
            },
        ),
        migrations.CreateModel(
            name='bug_client',
            fields=[
                ('bug_client_id', models.AutoField(primary_key=True, serialize=False)),
                ('bug_client_name', models.CharField(max_length=50)),
                ('bug_client_url', models.URLField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=5)),
                ('change_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bug_client_change_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bug_client',
            },
        ),
        migrations.CreateModel(
            name='list_of_bug_client',
            fields=[
                ('list_of_bug_client_id', models.AutoField(primary_key=True, serialize=False)),
                ('bug_client_name', models.CharField(max_length=50)),
                ('bug_client_api_url', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=5)),
                ('change_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_of_bug_client_change_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'list_of_bug_client',
            },
        ),
        migrations.RemoveField(
            model_name='api_access',
            name='change_user',
        ),
        migrations.DeleteModel(
            name='api_access',
        ),
        migrations.AddField(
            model_name='bug_client',
            name='list_of_bug_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NearBeach.list_of_bug_client'),
        ),
        migrations.AddField(
            model_name='bug',
            name='bug_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NearBeach.bug_client'),
        ),
        migrations.AddField(
            model_name='bug',
            name='change_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bug_change_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bug',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NearBeach.project'),
        ),
        migrations.AddField(
            model_name='bug',
            name='requirements',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NearBeach.requirements'),
        ),
        migrations.AddField(
            model_name='bug',
            name='tasks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NearBeach.tasks'),
        ),
    ]
