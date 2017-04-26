from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate
from fifa.models import Tournament
import mongoengine
import logging
log = logging.getLogger(__name__)


def home(request):
    create_user()
    return render(request, "home.html", {})


def save_tournament():
    name = "xyz"
    tournaments = Tournament.objects(tournament_name=name)
    if tournaments:
        log.error("tournament with name {0} already exists".format(name))
    else:
        log.info("creating tournament with name {0}".format(name))


def login_success(request):
    return render(request, "tournament.html", {})


def create_user():
    username = "pranith"
    password = "lol"
    user = authenticate(username=username, password=password)


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
    user = authenticate(username=username, password=password)
    assert isinstance(user, mongoengine.django.auth.User)


def register(request):
    return None




