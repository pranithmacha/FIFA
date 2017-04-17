# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 18:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('league', '0003_auto_20170402_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tournamentsummary',
            name='active',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='tournament_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='tournamentsummary',
            unique_together=set([('tournament', 'player')]),
        ),
    ]
