from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from league.models import Tournament, Team
from league.forms import RegistrationForm, TournamentForm
from league import tournaments_manager, user_manager
import logging

log = logging.getLogger(__name__)


@login_required
def home(request):
    user_id = request.user.id
    tournaments = tournaments_manager.get_tournaments_by_user(user_id)
    return render(request, "home.html", {"tournaments": tournaments})


@login_required
def create_tournament(request):
    if request.method == "GET":
        return render(request, "tournament.html", {})
    tournament_form = TournamentForm(request.POST, request=request)
    if tournament_form.is_valid():
        tournament_name = tournament_form.cleaned_data["tournament_name"]
        tournament_type = tournament_form.cleaned_data["tournament_type"]
        number_of_games = tournament_form.cleaned_data["number_of_games"]
        player_names = tournament_form.players
        players = list()
        tournament_type = "league"
        try:
            tournament = tournaments_manager.get_tournament_by_name(tournament_name)
            if tournament:
                log.error("tournament with name {0} already exists".format(tournament_name))
            else:
                log.info("creating tournament with name {0}".format(tournament_name))
                for user_name in player_names:
                    user = user_manager.get_user_by_username(user_name)
                    players.append(user)
                tournament = tournaments_manager.create_tournament(tournament_name, tournament_type,
                                                                   number_of_games, players)
                return redirect("get_tournament_summary", tournament_id=tournament.id)
        except AttributeError as e:
            log.error("could not create tournament with name {0}".format(tournament_name))
            log.exception(e)
    else:
        raise AttributeError("invalid form")


@login_required
def login_success(request):
    return redirect(to=reverse('home'))


def register(request):
    if request.method == "GET":
        return render(request, "register.html", {})
    user_name = None
    if request.method == "POST":
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            log.info("valid registration form")
            try:
                user_name = request.POST.get("user_name")
                email = request.POST.get("email")
                password = request.POST.get("password")
                confirm_password = request.POST.get("confirm_password")
                if password != confirm_password:
                    raise AttributeError("passwords do not match")
                profile = user_manager.create_user(user_name=user_name, password=password, email=email)
                log.info("user {0} successfully created".format(profile.username))
            except AttributeError as ae:
                log.exception(ae)
                error = ae.message
                return render(request, "register.html", {"error": error})
        else:
            error = "please fill all the required fields"
            return render(request, "register.html", {"error": error})
    return render(request, "login.html", {"registration_success": user_name})


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


def get_tournament_summary(request, tournament_id):
    tournament = tournaments_manager.get_tournament_by_id(tournament_id)
    summary = tournaments_manager.get_tournament_summary(tournament)
    for sum in summary:
        log.info(sum.player.username)
    return render(request, "tournament_summary.html", {"summary": summary})


def create_user(request):
    User.objects.create_user(username="abc", password="abc")


"""
{% for tournament in tournaments %}

{{tournament.tournament_name}}

{% endfor %}
"""






