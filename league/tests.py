from django.test import TestCase
from league.models import Tournament, TournamentSummary, GameSummary
from django.contrib.auth.models import User
from league import user_manager, tournaments_manager


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


class UserTestCase(TestCase):
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
        tournament = Tournament.objects.create(tournament_name="tiger",
                                               tournament_type="league", number_of_games=5,
                                               status=1)
        tournament.players = players
        tournament.save()

    def test_get_all_users(self):
        users = user_manager.get_all_users()
        self.assertEqual(2, len(users))

    def test_get_user_by_id(self):
        users = user_manager.get_all_users()
        for user in users:
            u_id = user.id
            looked_up_user = user_manager.get_user_by_id(u_id)
            self.assertEqual(looked_up_user.username, user.username)

    def test_get_user_by_email(self):
        users = user_manager.get_all_users()
        for user in users:
            u_email = user.email
            looked_up_user = user_manager.get_user_by_email(u_email)
            self.assertEqual(looked_up_user.username, user.username)

    def test_get_user_by_username(self):
        users = user_manager.get_all_users()
        for user in users:
            u_name = user.username
            looked_up_user = user_manager.get_user_by_username(u_name)
            self.assertEqual(looked_up_user.email, user.email)


class TournamentTestCase(TestCase):
    def setUp(self):
        player_one = User.objects.create_user(username="player_one",
                                              password="1234",
                                              email="playerone@gmail.com")
        player_two = User.objects.create_user(username="player_two",
                                              password="1234",
                                              email="playertwo@gmail.com")
        player_three = User.objects.create_user(username="player_three",
                                                password="1234",
                                                email="playerthree@gmail.com")
        players = [player_one, player_two, player_three]
        tournament_one = Tournament.objects.create(tournament_name="lion",
                                                   tournament_type="league", number_of_games=3,
                                                   status=1)
        tournament_one.players = players
        tournament_one.save()
        tournament_two = Tournament.objects.create(tournament_name="tiger",
                                                   tournament_type="league", number_of_games=5,
                                                   status=1)
        tournament_two.players = players
        tournament_two.save()

    def test_get_user_tournaments(self):
        user = user_manager.get_user_by_username('player_one')
        tournaments = tournaments_manager.get_tournaments_by_user(user.id)
        tournament_names = [tnmt.tournament_name for tnmt in tournaments]
        self.assertEqual(2, len(tournaments))
        self.assertListEqual(['lion', 'tiger'], tournament_names)

    def test_create_tournament(self):
        player_one = User.objects.create_user(username="player_oneone",
                                              password="1234",
                                              email="playerone@gmail.com")
        player_two = User.objects.create_user(username="player_twotwo",
                                              password="1234",
                                              email="playertwo@gmail.com")
        player_three = User.objects.create_user(username="player_threethree",
                                                password="1234",
                                                email="playerthree@gmail.com")
        players = [player_one, player_two, player_three]
        tournament_one = Tournament.objects.create(tournament_name="jaguar",
                                                   tournament_type="league", number_of_games=3,
                                                   status=1)
        tournament_one.players = players
        tournaments_manager.create_tournament(tournament_one, players)

        tournament = Tournament.objects.get(tournament_name='jaguar')
        self.assertEquals('jaguar', tournament.tournament_name)

        tournament_summary = TournamentSummary.objects.filter(tournament=tournament).select_related('player')
        count = 0
        for summary in tournament_summary:
            count += 1
            self.assertIsNotNone(summary.player)
        self.assertEqual(3, count)

    def test_save_gave_summary(self):
        player_one = user_manager.get_user_by_username("player_one")
        player_two = user_manager.get_user_by_username("player_one")
        tournament_one = Tournament.objects.create(tournament_name="elephant",
                                                   tournament_type="league", number_of_games=3,
                                                   status=1)
        game_summary = GameSummary()




