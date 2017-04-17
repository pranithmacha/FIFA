from django.test import TestCase
from league.models import Tournament, TournamentSummary
from django.contrib.auth.models import User


class TournamentTestCase(TestCase):
    def setUp(self):
        player_one = User.objects.create_user(username="player_one",
                                              password="1234",
                                              email="playerone@gmail.com")
        player_two = User.objects.create_user(username="player_two",
                                              password="1234",
                                              email="playertwo@gmail.com")
        players = [player_one, player_two]
        tournament = Tournament.objects.create(tournament_name="lion",
                                               tournament_type="league", number_of_games=3,
                                               status=1)
        tournament.players = players
        tournament.save()

    def test_tournament_creation(self):
        tournament_lion = Tournament.objects.get(tournament_name="lion")
        self.assertEqual(tournament_lion.tournament_type, 'league')


class TournamentSummaryTestCase(TestCase):
    def setUp(self):
        player_one = User.objects.create_user(username="player_one",
                                              password="1234",
                                              email="playerone@gmail.com")
        player_two = User.objects.create_user(username="player_two",
                                              password="1234",
                                              email="playertwo@gmail.com")
        players = [player_one, player_two]
        tournament = Tournament.objects.create(tournament_name="lion",
                                               tournament_type="league", number_of_games=3,
                                               status=1)
        tournament.players = players
        tournament.save()

        summary = TournamentSummary.objects.create(tournament=tournament, player=player_one)
        summary.played = 21
        summary.won = 15
        summary.lost = 3
        summary.drawn = 3
        summary.home_goals = 15
        summary.away_goals = 18
        summary.total_goals = 33
        summary.points = 48
        summary.save()

        summary_two = TournamentSummary.objects.create(tournament=tournament, player=player_two)
        summary_two.played = 19
        summary_two.won = 13
        summary_two.lost = 3
        summary_two.drawn = 3
        summary_two.home_goals = 14
        summary_two.away_goals = 8
        summary_two.total_goals = 22
        summary_two.points = 42
        summary_two.save()

    def test_tournament_summary_creation(self):
        tournament_lion = Tournament.objects.get(tournament_name="lion")
        self.assertEqual(tournament_lion.tournament_type, 'league')
        tournament_lion_summary = TournamentSummary.objects.filter(tournament=tournament_lion)
        self.assertEqual(len(tournament_lion_summary), 2)
        self.assertEqual(tournament_lion_summary[0].player.username, 'player_one')


class GameSummaryTestCase(TestCase):
    def setUp(self):
        player_one = User.objects.create_user(username="player_one",
                                              password="1234",
                                              email="playerone@gmail.com")
        player_two = User.objects.create_user(username="player_two",
                                              password="1234",
                                              email="playertwo@gmail.com")
        players = [player_one, player_two]
        tournament = Tournament.objects.create(tournament_name="lion",
                                               tournament_type="league", number_of_games=3,
                                               status=1)
        tournament.players = players
        tournament.save()

        summary = TournamentSummary.objects.create(tournament=tournament, player=player_one)
        summary.played = 21
        summary.won = 15
        summary.lost = 3
        summary.drawn = 3
        summary.home_goals = 15
        summary.away_goals = 18
        summary.total_goals = 33
        summary.points = 48
        summary.save()

        summary_two = TournamentSummary.objects.create(tournament=tournament, player=player_two)
        summary_two.played = 19
        summary_two.won = 13
        summary_two.lost = 3
        summary_two.drawn = 3
        summary_two.home_goals = 14
        summary_two.away_goals = 8
        summary_two.total_goals = 22
        summary_two.points = 42
        summary_two.save()

    def test_tournament_summary_creation(self):
        tournament_lion = Tournament.objects.get(tournament_name="lion")
        self.assertEqual(tournament_lion.tournament_type, 'league')
        tournament_lion_summary = TournamentSummary.objects.filter(tournament=tournament_lion)
        self.assertEqual(len(tournament_lion_summary), 2)
        self.assertEqual(tournament_lion_summary[0].player.username, 'player_one')






