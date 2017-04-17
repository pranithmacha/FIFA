# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_tournamentsummary_won'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesummary',
            name='player_one_goals',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gamesummary',
            name='player_two_goals',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tournamentsummary',
            name='away_goals',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tournamentsummary',
            name='drawn',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tournamentsummary',
            name='home_goals',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tournamentsummary',
            name='lost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tournamentsummary',
            name='played',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tournamentsummary',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tournamentsummary',
            name='total_goals',
            field=models.IntegerField(default=0),
        ),
    ]
