# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shakeitup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_name', models.CharField(max_length=100)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Song_On_Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs_on_playlists', to='shakeitup.Song')),
            ],
        ),
    ]