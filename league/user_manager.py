from django.contrib.auth.models import User
from league.models import Tournament
from django.db.utils import IntegrityError
import logging

log = logging.getLogger(__name__)


# IntegrityError
def get_all_users():
    """
    :return: list of all users
    """
    users = User.objects.all()
    return users


def get_all_users_by_pattern(pattern):
    """
    :type pattern: string pattern to search for
    :return: list of all users matching pattern
    """
    user = User.objects.filter(username__icontains=pattern)
    return user


def get_user_by_username(username):
    """
    :type username: username of the user to search
    """
    user = None
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist as ude:
        log.exception(ude)
    return user


def get_user_by_email(email):
    """
    :type email: object
    """
    user = User.objects.get(email=email)
    return user


def get_user_by_id(user_id):
    """
    :rtype: return user belonging to the id
    """
    user = User.objects.get(id=user_id)
    return user


def delete_user(user_id):
    """

    :rtype: boolean representing success or failure of delete
    """
    User.objects.filter(id=user_id).delete()
    return True


def update_user():
    pass


def create_user(user_name, email, password):
    try:
        user = User.objects.create_user(username=user_name, password=password, email=email)
    except IntegrityError as ie:
        log.error(ie)
        raise AttributeError("user {0} already exists".format(user_name))
    return user



