from django.db import models
from django.contrib.auth.models import User


class Tournament(models.Model):
    tournament_name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    tournament_type = models.CharField(max_length=200, blank=False, null=False)
    players = models.ManyToManyField(User)
    number_of_games = models.IntegerField(null=False, blank=False)
    created = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(null=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return "{0}".format(self.tournament_name)


class TournamentSummary(models.Model):
    tournament = models.ForeignKey(Tournament)
    player = models.ForeignKey(User)
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    drawn = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    total_goals = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    active = models.IntegerField(default=1)

    class Meta:
        unique_together = (("tournament", "player"),)


class Team(models.Model):
    team_name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    logo_name = models.CharField(max_length=200, blank=False, null=False)


class GameSummary(models.Model):
    tournament = models.ForeignKey(Tournament)
    player_one = models.ForeignKey(User, related_name="player_one")
    player_two = models.ForeignKey(User, related_name="player_two", default=None)
    player_one_goals = models.IntegerField(default=0)
    player_two_goals = models.IntegerField(default=0)
    player_one_team = models.ForeignKey(Team, related_name="player_one_team")
    player_two_team = models.ForeignKey(Team, related_name="player_two_team")
    result = models.CharField(max_length=200, blank=False, null=False)


class TournamentGameRecord(models.Model):
    tournament = models.ForeignKey(Tournament)
    player_one = models.ForeignKey(User, related_name="player_one_record")
    player_two = models.ForeignKey(User, related_name="player_two_record", default=None)
    games = models.IntegerField(default=0)

    class Meta:
        unique_together = (("tournament", "player_one", "player_two"),)


