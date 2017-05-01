from django.conf.urls import url
from league import views

urlpatterns = [
    url(r'^register', views.register, name='register'),
    url(r'^create_user', views.create_user, name='create_user'),
    url(r'^create_tournament', views.create_tournament, name='create_tournament'),
]
