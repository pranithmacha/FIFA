from django.conf.urls import url
from league import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^register', views.register, name='register'),
    url(r'^create_user', views.create_user, name='create_user'),
    url(r'^create_tournament', views.create_tournament, name='create_tournament'),
    url(r'^get_tournament_summary/(?P<tournament_id>[0-9])/', views.get_tournament_summary,
        name='get_tournament_summary'),
    url(r'^dialog1/$', TemplateView.as_view(template_name="dialog1.html"), name='dialog1'),
]
