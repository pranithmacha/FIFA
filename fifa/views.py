from django.shortcuts import redirect
from django.urls import reverse
import logging
log = logging.getLogger(__name__)


def login_success(request):
    return redirect(to=reverse('home'))

