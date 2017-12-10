from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from league.forms import RegistrationForm, TournamentForm, GameSummaryForm
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
        # tournament_type = tournament_form.cleaned_data["tournament_type"]
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
                    if not user:
                        raise AttributeError("could not find user {0}".format(user_name))
                    players.append(user)
                tournament = tournaments_manager.create_tournament(tournament_name, tournament_type,

                                                                   number_of_games, players)
                return redirect("get_tournament_summary", tournament_id=tournament.id)
        except AttributeError as e:
            log.error("could not create tournament with name {0}".format(tournament_name))
            log.exception(e)
    else:
        log.error("invalid form")
        return render(request, "tournament.html", {"error": "invalid form"})


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
def game_summary(request, tournament_id):
    if request.method == "GET":
        return render(request, "game_summary.html", {"tournament_id": tournament_id})
    game_summary_form = GameSummaryForm(request.POST)
    if game_summary_form.is_valid():
        player_one_name = request.POST.get("player_one")
        player_two_name = request.POST.get("player_two")
        player_one_goals = request.POST.get("player_one_goals")
        player_two_goals = request.POST.get("player_two_goals")
        player_one = user_manager.get_user_by_username(player_one_name)
        player_two = user_manager.get_user_by_username(player_two_name)
        tournament = tournaments_manager.get_tournament_by_id(tournament_id)
        tournaments_manager.save_game_summary(tournament, player_one, player_two,
                                              player_one_goals, player_two_goals)
        return redirect(reverse('get_tournament_summary', args=(tournament_id, )))
    else:
        log.error("invalid form")
        return render(request, "game_summary.html", {"tournament_id": tournament_id})


@login_required
def get_tournament_summary(request, tournament_id):
    tournament = tournaments_manager.get_tournament_by_id(tournament_id)
    summary = tournaments_manager.get_tournament_summary(tournament)
    for sum in summary:
        log.info(sum.player.username)
    return render(request, "tournament_summary.html", {"tournament_summary": summary,
                                                       "tournament_id": tournament_id})







