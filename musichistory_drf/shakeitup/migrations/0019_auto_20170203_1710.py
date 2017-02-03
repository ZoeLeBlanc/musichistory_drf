# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 17:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shakeitup', '0018_auto_20170203_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist_by_user',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_playlists', to=settings.AUTH_USER_MODEL),
        ),
    ]