from django.db import models


class Tournament(models.Model):
    tournament_name = models.CharField(max_length=200, blank=False, null=False)
    tournament_type = models.CharField(max_length=200, blank=False, null=False)
    players = models.CharField(max_length=200, blank=False, null=False)
