# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shakeitup', '0002_playlist_song_on_playlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song_on_playlist',
            name='song',
        ),
    ]
