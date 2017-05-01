from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from league.models import Tournament, TournamentSummary, Team
from django.db.utils import IntegrityError
from league.forms import RegistrationForm, TournamentForm
from league import tournaments_manager
import logging

log = logging.getLogger(__name__)


@login_required
def home(request):
    return render(request, "home.html", {})


@login_required
def save_tournament(request):
    tournament_form = TournamentForm(request.POST, request=request)
    if tournament_form.is_valid():
        pass
    tournament_name = "xyz"
    players = ""
    tournament_type = ""
    tournament_name = ""
    try:
        tournament = tournaments_manager.get_tournament_by_name(tournament_name)
        if tournament:
            log.error("tournament with name {0} already exists".format(tournament_name))
        else:
            log.info("creating tournament with name {0}".format(tournament_name))
            tournament = Tournament.objects.get(tournament_name=tournament_name,
                                                tournament_type=tournament_type, players=players)
            for username in players:
                try:
                    player = User.objects.get(username=username)
                    TournamentSummary.objects.create(tournament=tournament, player=player)
                except Exception as er:
                    log.exception(er)
                    log.error("could not find user with username {0}".format(username))
            return render(request, "", {"tournament": tournament})
    except Exception as e:
        log.error("could not create tournament with name {0}".format(tournament_name))
        log.exception(e)


@login_required
def login_success(request):
    return redirect(to=reverse('home'))


def register(request):
    if request.method == "GET":
        return render(request, "register.html", {})
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            log.info("valid registration form")
            user_info_dict = dict()
            try:
                user_info_dict["user_name"] = request.POST.get("user_name")
                user_info_dict["email"] = request.POST.get("email")
                user_info_dict["password"] = request.POST.get("password")
                user_info_dict["confirm_password"] = request.POST.get("confirm_password")
                profile = User.objects.create_user()
                log.info("user {0} successfully created".format(profile.username))
            except IntegrityError as ie:
                log.exception(ie)
                message = "username {0} already exists".format(user_info_dict["username"])
        else:
            pass
    else:
        log.error("invalid registration form")
    return render(request, "register.html", {})


@login_required
def save_game_summary(request):
    tournament_id = ""
    player_one_username = ""
    player_two_username = ""
    team_one_id = ""
    team_two_id = ""
    try:
        tournament = Tournament.objects.get(pk=tournament_id)
        player_one = User.objects.get(username=player_one_username)
        player_two = User.objects.get(username=player_two_username)
        player_one_team = Team.objects.get(pk=team_one_id)
        player_two_team = Team.objects.get(pk=team_two_id)
    except Exception as e:
        log.exception(e)


def create_user(request):
    User.objects.create_user(username="xyz", password="xyz")








