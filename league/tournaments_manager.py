from django.db import IntegrityError, transaction
from league.models import Tournament, TournamentSummary, TournamentGameRecord, GameSummary
import logging

log = logging.getLogger(__name__)


@transaction.atomic
def create_tournament(tournament_name, tournament_type, number_of_games, players):
    try:
        tournament = Tournament.objects.create(tournament_name=tournament_name,
                                               tournament_type=tournament_type,
                                               number_of_games=number_of_games,
                                               )
        tournament.players = players
        tournament.save()
        for player in players:
            TournamentSummary.objects.create(tournament=tournament, player=player)
    except Exception as ex:
        log.exception(ex)
        raise AttributeError
    return tournament


def get_tournaments_by_user(user_id, active=None):
    status = list()
    if active:
        status.append(1)
    elif not active and active is not None:
        status.append(0)
    else:
        status.append(1)
        status.append(0)
    tournaments = Tournament.objects.filter(players__id=user_id, status__in=status)
    return tournaments


def get_tournament_by_name(tournament_name):
    tournament = None
    try:
        tournament = Tournament.objects.get(tournament_name=tournament_name)
    except Tournament.DoesNotExist as e:
        log.exception(e)
    return tournament


def get_tournament_by_id(tournament_id):
    tournament = None
    try:
        tournament = Tournament.objects.get(pk=tournament_id)
    except Tournament.DoesNotExist as e:
        log.exception(e)
    return tournament


def get_tournament_summary(tournament):
    summary = TournamentSummary.objects.filter(tournament=tournament).select_related('player')
    return summary


@transaction.atomic
def save_game_summary(tournament, player_one, player_two, player_one_goals, player_two_goals):
    game_summary, created = GameSummary.objects.get_or_create(tournament=tournament,
                                                              player_one=player_one,
                                                              player_two=player_two,
                                                              player_one_goals=player_one_goals,
                                                              player_two_goals=player_two_goals)
    game_record, record_created = TournamentGameRecord.objects.get_or_create(tournament=game_summary.tournament,
                                                                             player_one=game_summary.player_one,
                                                                             player_two=game_summary.player_two)
    if game_record.games >= game_summary.tournament.number_of_games:
        raise AttributeError('max games played in this tournament between players {0} and {1}'
                             .format(game_summary.player_one.username, game_summary.player_two.username))
    game_record.games += 1
    game_record.save()
    player_one_tournament_summary = TournamentSummary.objects.get(tournament=game_summary.tournament,
                                                                  player=game_summary.player_one)
    player_two_tournament_summary = TournamentSummary.objects.get(tournament=game_summary.tournament,
                                                                  player=game_summary.player_two)
    player_one_tournament_summary.played += 1
    player_two_tournament_summary.played += 1
    player_one_tournament_summary.goals += int(player_one_goals)
    player_two_tournament_summary.goals += int(player_two_goals)
    if player_one_goals > player_two_goals:
        player_one_tournament_summary.won += 1
        player_one_tournament_summary.points += 3
        player_two_tournament_summary.lost += 1
        result = "{0} won".format(player_one.username)
    elif player_one_goals < player_two_goals:
        player_two_tournament_summary.won += 1
        player_two_tournament_summary.points += 3
        player_one_tournament_summary.lost += 1
        result = "{0} won".format(player_one.username)
    elif game_summary.player_one_goals == game_summary.player_two_goals:
        player_one_tournament_summary.drawn += 1
        player_two_tournament_summary.drawn += 1
        player_one_tournament_summary.points += 1
        player_two_tournament_summary.points += 1
        result = "draw"
    player_one_tournament_summary.save()
    player_two_tournament_summary.save()
    game_summary.result = result
    game_summary.save()


def get_tournamnet_summary_for_player(player, tournament):
    tournament_summary_for_player_one = TournamentSummary.objects.get(tournament=tournament, players__id=player.id)
    return tournament_summary_for_player_one
